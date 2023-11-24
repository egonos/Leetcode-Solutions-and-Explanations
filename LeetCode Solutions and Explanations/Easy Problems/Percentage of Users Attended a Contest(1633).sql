/*Intuition
Lets look at what my solution does:

Picks contest_id and different user_id counts from register table.
Divides this count to the length of the users table and multiplies with 100.
Does this process for each contest_id.
Finally orders the result accordant to the question requirements.
The final code looks like this:

Final Code*/

select  contest_id, round(count(distinct user_id)*100/(select count(*) from users),2) as percentage from register
group by contest_id
order by percentage desc, contest_id asc;