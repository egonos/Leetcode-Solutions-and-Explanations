/*
Explanation: 
To roundup 2 digits, we can use ROUND(...,2)
To find the sum of all the values in a column, we can use SUM()
*/

SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2) FROM STATION 