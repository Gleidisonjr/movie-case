SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS customer_name,
    MIN(r.rental_date) AS first_rental,
    MAX(r.rental_date) AS last_rental,
    COUNT(r.rental_id) AS total_rentals,
    SUM(p.amount) AS total_spent,
    DATE_PART('day', MAX(r.rental_date) - MIN(r.rental_date)) AS customer_lifetime_days
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY c.customer_id, customer_name