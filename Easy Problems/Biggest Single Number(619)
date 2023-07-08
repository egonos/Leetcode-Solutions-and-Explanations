/*
Intuition
Let's go over the code:

select max(num) as num from 
* select the maximum number from a table (not the table because maximum of a number groupby function is the number itself)

(select num from mynumbers group by num having count(*) = 1) as singles;
* Take the same column and group it according to the numbers then count the number of occurances of each finally pick only the ones occured once in the original table.

Final Code:
*/
select max(num) as num from 
(select num from mynumbers 
group by num
having count(*) = 1) as singles;