/*
SQLite Solution
----------

*/

with cte as (select customer_id,min(order_date) as first_order,customer_pref_delivery_date as del_date from delivery
group by customer_id)

SELECT 
    round(SUM(
        CASE 
            WHEN date(del_date, '-1 day') = first_order THEN 1
            ELSE 0
        END
    ) *100 / COUNT(*),2) AS immediate_percentage  
FROM cte;