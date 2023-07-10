/*Intuition
Here is my solution:

Select query name first.
Find the ratio between rating and position and get the average using avg(), finally round it up.
To check whether a given percentage of query rating less than 3, I've used if operator. If that iss the case the output is 1; 0 otherwise.
Sum all the ones and divide it into the number of occurances for each group.
Final Code*/

select query_name, round(avg(rating/position),2) as quality, round(100*sum(if (rating < 3, 1,0))/count(*),2)  as poor_query_percentage from queries
group by query_name;Queries Quality and Percentage(1211(