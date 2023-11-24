/*
To round up: ROUND()
For the conditional statement: WHERE()
To get the minimum: MIN()
*/

select round(min(lat_n),4) from station where lat_n > 38.7780;