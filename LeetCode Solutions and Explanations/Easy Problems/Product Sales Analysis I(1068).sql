/*
Intuition
Hi everyone. Fpr this problem, we need to merge two tables utilizing the common column product_id then return the required columns:
*/

select product_name,year,price from sales s
inner join product p on p.product_id = s.product_id;