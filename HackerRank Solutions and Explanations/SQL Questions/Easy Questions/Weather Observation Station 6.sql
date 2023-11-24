/*
To eliminate the duplicates: distinct
To pick the first letter: substr(city,1,1)
To check if the first letter is a vowel: in ('a','e','i','o','u') 
*/

select distinct city from station where substr(city,1,1) in ('a','e','i','o','u');