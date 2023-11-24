/*
By using inner join, we can combine the data from both tables. {city.countrycode = country.code} 
Then select sum of the population from this combined table.
Finally, we need to filter the result by adding {where country.continent = 'Asia'}.
*/


select sum(city.population) from city inner join country on city.countrycode = country.code where country.continent = 'Asia';