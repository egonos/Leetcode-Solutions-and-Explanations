/*
First, we need to find the minimum lat_n grater than 38.7780. For this, between the paranthesis, we use
min(): to find the minimum value
where(): to define the condition

Then all we need to do is to search for the associated value and to return the corresponing long_w value after rounding it up.
*/


select round(long_w,4) from station where lat_n = (select min(lat_n) from station where lat_n>38.7780); 