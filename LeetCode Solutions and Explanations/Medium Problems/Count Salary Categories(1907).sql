/*
Hi everyone. Including  salary category having zero count in the result is the most challenging part.
If our duty is only finding the count of the salary categories, we could use the following query (my initial solution by the way):
*/

select case
                    when income <20000 then "Low Salary"
                    when income >= 20000 and income <= 50000 then 'Average Salary'
                    when income > 50000 then 'High Salary'
                    end
                     as category, count(*) as accounts_count from accounts
group by category;

/*
To fix the issue I've encountered, I've used CTEs. First I've created a CTE with the salary categories.
Then I've created another CTE with the salary categories and the count of the accounts for each category.
Finally I've joined the two CTEs to get the correct result (I've used `coalesce()` to handle null values).

My final code looks like this:
*/

with cte as(select 'Low Salary' as category
union
select 'Average Salary' as category
union
select 'High Salary' as category),

cte2 as (select case
                    when income <20000 then "Low Salary"
                    when income >= 20000 and income <= 50000 then 'Average Salary'
                    when income > 50000 then 'High Salary'
                    end
                     as category, count(*) as accounts_count from accounts
group by category)

select cte.category,coalesce(cte2.accounts_count,0) as accounts_count from cte 
left join cte2 on cte.category = cte2.category
;