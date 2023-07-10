/*
Intuition
Hi everybody! For this problem I've applied the following
(1)
*/
select e.name as name, b.bonus as bonus
/*
pick the name from employee table and pick the bonus from bonus table.
(2)
*/
from employee e left join bonus b on e.empid = b.empid 
/*
Form a union by matching the empid columns of each table.
(3)
*/
where bonus < 1000 or bonus is null;
/*
define the conditions.

All together resulted in this solution:
*/
select e.name as name, b.bonus as bonus from employee e left join bonus b 
on e.empid = b.empid 
where bonus < 1000 or bonus is null;