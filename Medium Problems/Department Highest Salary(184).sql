/*
Hi everyone! Here is my approach.
We need to select department name, employee name and salary of the employee with highest salary in each department.
So first I've selected these columns. Since all of the columns are not present on one table I've merged the `employee` and `department` tables.
We have to pick only the rows containing max salary. To code it I've used where.
The `where` command looks on a table I've created. THe reference table consists maximum salaries of each department.
Here is the final code:
*/

select 
d.name as Department,
e.name as employee,
e.salary as Salary
from employee e
inner join department d on d.id = e.departmentid

where (e.departmentid,e.salary) in

(select e.departmentid,max(e.salary) from employee e
group by departmentid);

