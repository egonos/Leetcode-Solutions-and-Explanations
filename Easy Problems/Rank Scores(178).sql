/*Intuition
Hi everyone. This is the first time that I've used the dense_rank() in my SQL journey. Here is what I've learned from my trial and errors and investgations on dense_rank:

The format:
dense_rank() over (what and how to rank) as column_name in ''

Ordering: Since the highest score has the lowest ranking (4,00 -> 1) we need to order the scores in descending order. Otherwise highest score gets highest ranking which is wrong.
The final code looks like this:

Code*/

select score, (dense_rank() OVER (order by score desc)) as 'rank' from scores
order by score desc;