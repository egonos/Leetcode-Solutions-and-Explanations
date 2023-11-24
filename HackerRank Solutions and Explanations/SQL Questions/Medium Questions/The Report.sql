/*
We have to first select the required variables:
1. The name of the student if the grade is greater than or equal to 8
2. NULL if the grade is less than 8
    The case statement does this for us.
3. The grade (g.grade)
4. The marks (s.marks)

Then we have to join the two tables on the condition that the marks of the student are between the minimum and maximum marks of the grade.
* inner join grades g on s.marks between g.min_mark and g.max_mark

Finally, we have to order the result by the grade in descending order and then by the marks in ascending order if the grade is less than 8, else by the name of the student in ascending order.
* order by g.grade desc, case when g.grade < 8 then s.marks else s.name end;
*/

select case
    when g.grade < 8 then 'NULL'
    else s.name
    end
, g.grade,s.marks from students s inner join grades g
on 
s.marks between g.min_mark and g.max_mark
order by
g.grade desc,
case
    when g.grade < 8 then s.marks
    else s.name
end;