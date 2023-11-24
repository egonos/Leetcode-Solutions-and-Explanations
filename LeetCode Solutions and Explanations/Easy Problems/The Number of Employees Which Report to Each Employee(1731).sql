/*Intuition
Hi everyone. For this problem, we need to do the following:

Merge the table by itself by matching reports_to with employee_id. This way we can easily compute the averages.
All we have to do after this point is to group and order the merged table by employee_id. count(*) will count the number of rows for each employee. We will rename this value as "reports_count" and round(avg(e2.age)) will calculate the average ages and round the value to it's nearest integer. We will take this value also and rename it as "average_age".
The final code looks like this:

Final Code*/

select e1.employee_id,e1.name,count(*) as reports_count, round(avg(e2.age)) as average_age from employees e1
inner join employees e2 on e1.employee_id =  e2.reports_to
group by employee_id
order by employee_id;