/*
Explanation:
To truncate 4 digits, we can use ROUND(...,4)
To find the sum of all the values in a column, we can use SUM()
*/

SELECT ROUND(SUM(LAT_N),4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345 ;