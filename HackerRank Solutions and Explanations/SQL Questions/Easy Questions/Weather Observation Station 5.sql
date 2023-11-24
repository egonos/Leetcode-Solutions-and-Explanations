/*
Explanation:
To get the max and min cities we have to order them by length and pick the first one after sorting them accordingly.
length(): Returns the length of the string
city asc: To pick the  first city alphabetically in case of a tie
*/

select city, length(city) from station order by length(city) asc, city asc limit 1;

select city, length(city) from station order by length(city) desc, city asc limit 1;