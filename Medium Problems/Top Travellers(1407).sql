/*Intuition
Hi everyone. Here is my solution.

To include zero distances, we need to use left join. However, the result we obtain solely using left join is "NULL". To convert it to 0, we can use coalesce.
After merging the tables, the best way to group the data is using id's. Why? Because, different people could potentially have the same name. This will make our result wrong. When we use id's instead, it won't be an issue anymore.
Finally we need to first order the data by distance travelled in descending order, second the names in ascending order like I've done in 5th line.
Final Code*/

select u.name, coalesce(sum(r.distance),0) as travelled_distance from users u
left join rides r on r.user_id = u.id
group by u.id,u.name
order by travelled_distance desc, name asc;