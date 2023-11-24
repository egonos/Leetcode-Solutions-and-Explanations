/*
Intuition
Hi everybody! Here is the step by step explanation:

(1) select name, population, area from world

Select the required features from the table
(2) where area >= 3000000 or population >= 25000000;

Select only the ones obeying the criterias stated.
Resulting:
*/

select name, population, area from  world
where
      area >= 3000000  or
      population >= 25000000;