from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import psycopg2
import logging

default_args = {
    'owner': 'junior',
    'start_date': datetime(2024, 1, 1),
}

def run_cdc():
    try:
        conn = psycopg2.connect(
            host="postgres",
            port="5432",
            database="movie_landing",
            user="postgres",
            password="postgres"
        )
        cur = conn.cursor()

        cur.execute("""
            WITH last_run AS (
              SELECT last_loaded FROM cdc_control WHERE table_name = 'rental'
            )
            INSERT INTO rental
            SELECT *
            FROM rental_staging r, last_run l
            WHERE r.last_update > l.last_loaded;
            UPDATE cdc_control
            SET last_loaded = (SELECT MAX(last_update) FROM rental_staging)
            WHERE table_name = 'rental';
        """)
        logging.info("CDC para rental concluído com sucesso.")

        cur.execute("""
            WITH last_run AS (
              SELECT last_loaded FROM cdc_control WHERE table_name = 'payment'
            )
            INSERT INTO payment
            SELECT *
            FROM payment_staging p, last_run l
            WHERE p.payment_date > l.last_loaded;
            UPDATE cdc_control
            SET last_loaded = (SELECT MAX(payment_date) FROM payment_staging)
            WHERE table_name = 'payment';
        """)
        logging.info("CDC para payment concluído com sucesso.")

        conn.commit()
        cur.close()
        conn.close()

    except Exception as e:
        logging.error("Erro ao executar o CDC: %s", str(e))
        raise

with DAG(
    dag_id="cdc_rental_payment_dag",
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args,
    description="Executa o CDC das tabelas rental e payment"
) as dag:
    run_cdc_task = PythonOperator(
        task_id="run_cdc",
        python_callable=run_cdc
    )