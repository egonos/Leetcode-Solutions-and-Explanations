/*
Intuition
Let's again cover the code step by step:

select sp.name from salesperson sp
* pick the name column from salesperson table.

where not exists
* If the following statements are false then apply the reverse.

(select 1 from orders o inner join company c on c.com_id = o.com_id
* merge the orders table with company table on com_id column

where o.sales_id = sp.sales_id and c.name = 'RED');
* only consider the rows in which sales_id values belong to orders and salesperson table are the same. Besides that company name also should be 'RED'.

-> If there is an instance in which the company name is 'RED' and there is a transaction, NOT EXISTS statement becomes False therefore the salesperson in consideration excluded from the answer. In this way we also consider the people having no orders.

The final code:
*/

select sp.name
from salesperson sp
where not exists(
  select 1
  from orders o
  inner join company c on c.com_id = o.com_id
  where o.sales_id = sp.sales_id and c.name = 'RED');