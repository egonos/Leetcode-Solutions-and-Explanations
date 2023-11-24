/*Intuition
Hi everyone. After many trials I've found the correct solution. Here is what I've learned:

WE can not include count in where statement. Therefore we need to define two separate subqueries and unite them. THe first condition, `primary_flag = 'Y' can be stated with where. Therefore I've done in this way. After that, I've used having to count the occurances for each employee_id.
The final code looks like this:

Code*/

select employee_id,department_id from employee where primary_flag = 'Y' 
union
select employee_id,department_id from employee 
group by employee_id
having count(*) = 1;