/*
Explanation
First, we obtained the combined table by matching country code from city with code from country.
Second, we pick African city names from the combined table.
Fİnally we filter the result by adding {where country.continent = 'Africa'}.

Note: To round up to nearest integer floor() should be used not round(). 
*/


select country.continent, floor(avg(city.population)) from city inner join country on city.countrycode = country.code group by country.continent;