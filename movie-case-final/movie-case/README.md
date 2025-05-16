
# 🎬 Case Analista de Dados — MovieStream Analytics

Este repositório contém a solução completa para o desafio proposto pela empresa fictícia **MovieStream Analytics**.  
O objetivo é construir uma pipeline robusta para ingestão, tratamento, modelagem e visualização de dados de uma aplicação de locação de filmes.

---

## 🚀 Visão Geral da Solução

### ✔️ Tecnologias Utilizadas

- PostgreSQL (Docker)
- Apache Airflow (CDC Orquestrado)
- DBT (Data Build Tool)
- Python
- DBeaver
- Matplotlib (para gráficos)
- PowerPoint/PDF (painel substituto do Qlik)

---

## 🔁 Pipeline de Ingestão

- Dump do banco restaurado via Docker: `voxtecnologiahub/dbinterview`
- Dados extraídos da base `dbinterview` para `movie_landing`
- Implementada estratégia de **CDC** para as tabelas `rental` e `payment`
- DAG `cdc_rental_payment_dag` criada no Airflow para ingestão incremental diária

---

## 🏗️ Modelagem com DBT

Projeto `movie_dbt` com os seguintes modelos:

| Modelo                          | Descrição                                                       |
|---------------------------------|------------------------------------------------------------------|
| `mart_customer_lifetime_value` | Total gasto por cliente e tempo de relacionamento               |
| `mart_film_popularity`         | Filmes mais alugados por volume total                           |
| `mart_store_performance`       | Receita e volume de clientes por loja                           |

---

## 🧠 Análises SQL

Consultas analíticas desenvolvidas com base no modelo:

- Top 5 clientes que mais geraram receita no último ano
- Média de dias entre aluguel e devolução por categoria
- Top 3 cidades com maior volume de locações
- Ticket médio por loja
- Receita mensal dos últimos 24 meses

Todas as queries seguem o padrão SQL PostgreSQL.

---

## 📊 Visualização & Storytelling

Devido à expiração do ambiente Qlik Sense em minha máquina na versão de meio, foi entregue um painel substituto simples utilizando python e pdf:

✅ **[Painel Executivo em PDF](Painel_MovieStream_Analytics.pdf)**  
Contém:
- Gráficos com insights por cliente, filme e loja
- Texto explicativo com storytelling estratégico

---

## 🗂️ Estrutura do Projeto

```
movie-case/
├── dags/
│   └── cdc_rental_payment_dag.py
├── movie_dbt/
│   ├── dbt_project.yml
│   └── models/
│       ├── mart_customer_lifetime_value.sql
│       ├── mart_film_popularity.sql
│       └── mart_store_performance.sql
├── Painel_MovieStream_Analytics.pdf
├── docker-compose.yaml
└── README.md
```

---

## 🧪 Extras

- Versão básica de teste implementada via `dbt run`
- Variáveis e conexões externas separadas no `profiles.yml` local
- Painel substituto entregue via PDF (Versão maio do Qlik Desktop não foi possível de ser instalada em meu escritório)

---

## 👤 Autor

**Gleidison Antônio de Carvalho Júnior**  
Analista de Dados | Cientista de Dados Projeto desenvolvido como parte de processo seletivo da VOX Tecnologia
Contato: gleidisonjunior187@gmail.com
Linkedin: https://www.linkedin.com/in/gleidisonjr/
Portfólio: https://www.datascienceportfol.io/gleidisonjunior187

---

## ✅ Status: Finalizado
