/*
Explanation: 
We pick African city names from the combined table.
The combined table is obtained by matching country code from city with code from country. 
Fİnally we filter the result by adding {where country.continent = 'Africa'}. 
*/

select city.name from city inner join country on country.code = city.countrycode where country.continent = 'Africa';