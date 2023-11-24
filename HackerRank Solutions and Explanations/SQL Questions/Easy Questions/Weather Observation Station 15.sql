/*
First we need to find the largest lat_n smaller than 137.2345. For that purpose between paranthesis we need to define the necessary conditions and add select in front of it to pick the value. After finding the maximum value, we need to assign it as the lookup value {lat_n = (select... }. Lastly, to round up, we need to use ROUND().
*/

select round(long_w,4) from station where lat_n = (select max(lat_n) from station where lat_n < 137.2345);