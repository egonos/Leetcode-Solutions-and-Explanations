/*Intuition
Hi everyone. For this problem, we need the following:

Select the required columns and compute the required processes (1st line)
Merge the tables (2nd line)
Filter the February Data (3rd line)
Filter the 100+ units (5th line)
Group the remaining data according to the product_id (4th line)
The Code*/

select p.product_name, sum(o.unit) as unit from products p
inner join orders o on o.product_id = p.product_id
where o.order_date >= '2020-02-01' and o.order_date <= '2020-02-29'
group by p.product_id
having unit >= 100;