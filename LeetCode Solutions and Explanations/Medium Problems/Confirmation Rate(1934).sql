/*
Hi everybody. Here is how I've solved this question.
First of all we need to pick `user_id` from `Signups` table because it may contain users who does not appear in the confirations rable (6 for example).
Secondly, since `Confirations.action` is not numeric I've created a cte and converted action values to binary values (0 for timeout, 1 for confirmed).
Then I've joined the two tables and calculated the average of the binary values. (Don't forget to round up the result to 2 decimal places!)
Finally I've used `coalesce()` to handle null values (natural consequence of left join).

*/


with cte as (select confirmations.user_id,case 
            when confirmations.action = 'timeout' then 0
            when confirmations.action = 'confirmed' then 1
            end as counts from confirmations)

select s.user_id, coalesce(round(avg(cte.counts),2),0) as confirmation_rate from signups s
left join cte on s.user_id = cte.user_id 
group by s.user_id;