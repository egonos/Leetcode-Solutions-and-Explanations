/*
Intuition
Hi everyone. Lets go over the code together:

select actor_id, director_id from 
* We are selecting the required columns

(select actor_id,director_id,timestamp from actordirector group by actor_id, director_id having count(timestamp) >=3) as newtable
or

actordirector group by actor_id, director_id having COUNT(*) >= 3;
* In here, we can write a subquery and get results from that or we can take it from original table. Both of them do the same thing:

->Group the table based on actor_id and director_id
->Filter the result based on occurence counts.

My First Solution
*/
select actor_id, director_id from 
(select actor_id,director_id,timestamp from actordirector
group by actor_id, director_id
having count(timestamp) >=3) as newtable;

/*My Second Solution*/
select actor_id, director_id from ActorDirector 
group by actor_id, director_id
having count(*) >= 3;