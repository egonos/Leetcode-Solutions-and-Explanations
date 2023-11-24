/*
Explanation
substr(...,1,1): to get the first character of the job
concat(...): To merge the input between paranthesis.
order by count(occupation), occupation asc: First order by count then by occupation in ascending order.
*/


select concat(name, '(', substr(occupation,1,1), ')') from occupations order by name asc;
select concat('There are a total of ', count(occupation), ' ', lower(occupation), 's.') from occupations group by occupation order by count(occupation), occupation asc; 