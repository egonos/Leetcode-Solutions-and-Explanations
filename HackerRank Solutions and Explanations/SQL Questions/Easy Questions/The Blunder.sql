/*
Explanation
The question statement tells us to replace all the 0's in the salary column with nothing and then find the average of the salaries.
ROUND() -> To round up the averages
REPLACE() -> To replace the 0's with nothing
AVG() -> To find the average of the salaries. 
*/
Solution
SELECT(ROUND(AVG(SALARY)) - ROUND(AVG(REPLACE(SALARY,'0','')))) FROM EMPLOYEES; 