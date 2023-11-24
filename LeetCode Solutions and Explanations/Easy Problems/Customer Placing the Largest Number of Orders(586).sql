/*
Intuition
Hi everybody! Let's go step by step:

(1) select customer_number from orders

We need to return a customer number therefore we need to select that variable.
(2) group by customer_number

Before counting the number of orders we need to group the customers so that the result would be customer basis.
(3) order by count(order_number) desc

After counting the number of orders for each customer order them in descending order.
(4) limit 1

return the first one.
Resulting:
*/

select customer_number from orders
group by customer_number
order by count(order_number) desc
limit 1;