/*Intuition
The key point of this problem is to determine the grouping objective correctly so that the total_time caluclation would be conducted correctly. In this case we need to group the data first event date so that we can find the total_time for each day. Can we leave it like that? Of course no. Because if we leave it like that sql will calculate combined sum for each day. We can prevent this to happen by defining a second grouping objective, emp_id. What does it serve to us? It tells sql to calculate the individual total_time for each day which we need to do to create the correct table.

The final code looks like this:

Code*/

select event_day as day, emp_id, sum(out_time - in_time) as total_time from employees
group by event_day,emp_id;