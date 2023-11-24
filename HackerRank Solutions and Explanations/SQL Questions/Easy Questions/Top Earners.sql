/*
Explanation:

We need to count the number of max earners. To do that we enter the formula (salary * months) and add COUNT(*) to count the number of max earners. Earnings to be looked is the maximum earnings.
salary*months = (SELECT MAX(salary*months) FROM employee) Only increase count if the salary*months is equal to the maximum earnings.
*/


SELECT MAX(SALARY * MONTHS), COUNT(*) FROM EMPLOYEE WHERE SALARY*MONTHS = (SELECT MAX(SALARY*MONTHS) FROM EMPLOYEE);
SELECT MAX(SALARY * MONTHS), COUNT(*) FROM EMPLOYEE WHERE SALARY * MONTHS = (SELECT MAX(SALARY* MONTHS) FROM EMPLOYEE);