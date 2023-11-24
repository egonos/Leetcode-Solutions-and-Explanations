/*
Hi everyone. Here is how I've solved this question. 
We need to find the user who has rated the most movies and the movie with the highest average rating in February 2020.
For that purpose we need to code two distinct queries and unite them.
The first query picks the first name from an subquery which counts the number of ratings for each user and orders them in descending order.
In between the queries we use the UNION ALL operator to unite the results of the two queries. We use UNION ALL because we want to keep the duplicate values.(One test case fails otherwise)
The second query picks the first title from a subquery which calculates the average rating for each movie and orders them in descending order.
For both the queries we use the LIMIT 1 clause to pick the first (intended) result.
*/



(select name  as results from (
select u.name, count(*) as rating_counts from users u inner join movierating mr
on mr.user_id = u.user_id
group by u.user_id order by rating_counts desc, u.name) as results limit 1) 

union all

(select title from (
select m.title,avg(mr.rating) as avg_rating from movies m inner join movierating mr 
on mr.movie_id = m.movie_id where mr.created_at < '2020-03-01' and mr.created_at >= '2020-02-01'
group by m.movie_id
order by avg_rating desc, title) as results limit 1 ) ;