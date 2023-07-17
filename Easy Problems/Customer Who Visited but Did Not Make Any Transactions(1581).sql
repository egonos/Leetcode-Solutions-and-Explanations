/*
Hi everyone, here is my approach.
We need to select customer_id and count of "no" transactions for each customer.
To do that, we need to include non transaction visits to our table. Because of that we need to use `left join`.
After merging the tables, all we need to do is filter the null rows (we can use `transaction_id`, `amount` or `visit_id` for that).
Finally we need to group the rows by `customer_id` to get the no transaction output for each customer.
Here is the final code:
*/

select v.customer_id,count(*) as count_no_trans from visits v left join transactions t on v.visit_id = t.visit_id
where t.amount is null
group by v.customer_id; 
