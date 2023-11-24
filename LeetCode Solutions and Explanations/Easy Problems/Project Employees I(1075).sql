/*Intuition
Hi everyone. Lets go over the code one by one:

select project_id, round(avg(experience_years),2) as average_years
* First select the required outputs from the project table.

from project p inner join employee e on e.employee_id = p.employee_id
* Since all the columns do not present in the products table we need to merge it with employee table.

group by project_id;
* To calculate the averages we need to group the data. The right choice for this problem is project_id variable.

Final Code*/

select project_id, round(avg(experience_years),2) as average_years from project p
inner join employee e on e.employee_id = p.employee_id
group by project_id;