/*
Hi everyone. Here is my solution:
We need to combine the `accepter_id` and `requester_id` columns into one column first so that we can count the number of times each id appears in the combined column.
Why do we want something like this? Because we want to know who has the most friends. The more friends you have, the more times your id will appear in either `accepter_id` or `requester_id` columns.
To combine the columns I've used `union all`. (We want to keep the duplicates so `union` won't work here.)
After that I've used `group by` and `count` to count the number of times each id appears in the combined column.
To return only the most popular id I've used limit 1.

Here is the final code:
*/

with cte as (select requester_id as id, count(requester_id) as num from (
(select requester_id from RequestAccepted)
union all
(select accepter_id  from RequestAccepted)) as helper
group by id)

select id,num from cte 
order by num desc
limit 1;
