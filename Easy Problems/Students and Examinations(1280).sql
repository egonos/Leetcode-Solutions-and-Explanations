/*Intuition
Hi everyone. This code was hard for me but I finally did it. Here is how

We need to select the required columns from the tables
Here is the part that I have struggled the most. We need to count student id's because the left join operation includes "NULL" values in the table giving the wrong results. On the other hand counting student id's includes these Null values in counting operation which is something we want. (There are zeros on the right output)
cross join is the join operatin we need to utilize when merging subjects and students table because the result of this operation is
student1......... subject1
student1......... subject2
student1......... subject3

student2......... subject1
student2......... subject2
student2......... subject3
similar to the correct output (all combinations).

The other join operation should be left join because we want the union of the results not intersections. Using inner join automatically eliminates the "NULL" values.
Grouping should be based on first student_id's and second subject name.
Finally we need to order the result by student id.
The final code:*/

select s.student_id,s.student_name,su.subject_name, count(e.student_id) as attended_exams from students s
cross join subjects su
left join examinations e on e.subject_name = su.subject_name and e.student_id = s.student_id
group by s.student_id,su.subject_name
order by s.student_id; 