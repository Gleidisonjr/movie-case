SELECT
    s.store_id,
    a.address,
    COUNT(DISTINCT c.customer_id) AS total_customers,
    SUM(p.amount) AS total_revenue
FROM store s
JOIN address a ON s.address_id = a.address_id
JOIN customer c ON s.store_id = c.store_id
JOIN payment p ON c.customer_id = p.customer_id
GROUP BY s.store_id, a.address
ORDER BY total_revenue DESC