/*
Intuition
Hi everyone. Let's observe the solution step by step:

select class from courses

* We need to return class variable.That's why we are selecting this feature from the original table.

group by class

* Before counting the number of students per class we need to group them.

having count(student)>=5;

* The code above tells only pick the classes having more than 5 students.

Final code:
*/

select class from courses
group by class
having count(student)>=5;