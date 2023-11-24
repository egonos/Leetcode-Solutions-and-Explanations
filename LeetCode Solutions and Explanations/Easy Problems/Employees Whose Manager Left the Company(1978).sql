/*Intuition
In my code, I've checked the following:

The salary is less than 30000 and the salary is not null.
The manager_id in consideration not in employee_id (The manager left from the company)
Finally I've ordered the results by employee_id in ascending order
Code*/

select employee_id from employees where 
salary < 30000 and
salary is not null and
manager_id not in (select employee_id from employees)
order by employee_id;