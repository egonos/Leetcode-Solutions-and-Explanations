/*
Intuition
Hi everyone. Lets go step by step again:

select x,y,z
* select all the columns from the triangle table.

case when x+y>z and x+z>y and y+z>x then 'Yes' else 'No' end as triangle from triangle;
* Define the necessary conditions for a triangle to exists the determine the outputs based on the correctness of these statements

Final Code:
*/
select x,y,z, case
              when x+y>z and x+z>y and y+z>x then 'Yes'
              else 'No' 
              end
              as triangle
from triangle;