/*
The most important thing for this problem ist to order the conditions correctly. For instance, in my first trial I put "Not a Triangle" statement at the end and it resulted in wrong outputs to form. We first need to check whether it is a valid triangle then determine it's type.
*/

select case
    when A+B <= C or B+C <= A or A+C <= B then'Not A Triangle'
    when A = B and B = C then 'Equilateral'
    when A = B or B = C or A = C then 'Isosceles'
    when A <> B and B <> C then 'Scalene'
    
    end
    
from triangles;