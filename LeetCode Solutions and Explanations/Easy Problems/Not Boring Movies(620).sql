/*
Intuition
Let's go oner the code:

select * from cinema
* Select all the columns from the cinema

where id %2 = 1 and description <> 'boring'
* If the id is odd (modulus 2 is 1) and description is not boring.

order by rating desc;
* order the result by rating in descending order.

Final Code:
*/
select * from cinema
where id %2 = 1 and description <> 'boring'
order by rating desc;