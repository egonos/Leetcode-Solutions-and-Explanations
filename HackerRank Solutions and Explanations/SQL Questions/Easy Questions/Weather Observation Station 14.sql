/*
To get max: MAX()
For truncating: TRUNCATE(...,4)
For conditional stateement: WHERE()

Note: ROUND() and TRUNCATE() are different from each other. For example:

37.34567
Round to two decimal places: 37.35
Truncate to two decimal places: 37.34

*/

select truncate(max(lat_n),4) from station where lat_n< 137.2345;