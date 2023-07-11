/*Intuition
Hi everyone. Here is my solution:

We know that to include null values, we need to prefer left_join.
Another thing we have to keep in mind is that left_join only preserves the values of only one table. We need to preserve the values of both employees and salary table. That's why I've interchangably used the left_join then united the results.
My final code looks like this:

Code*/

select e.employee_id from employees e
left join salaries s on s.employee_id = e.employee_id
where e.name is null or s.salary is null
union
select s.employee_id from salaries s
left join employees e on s.employee_id = e.employee_id
where e.name is null or s.salary is null
order by employee_id; 