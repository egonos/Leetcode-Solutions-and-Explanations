/*
We have to objectives: Minimize the cost of the wand and maximize the power of the wand.
To consider both objectives we need to:
1. Eliminate the wands that are evil. (where wp.is_evil = 0)
2. For each power and age, we need to select the wand with the minimum cost. min(w.coins_needed),(group by w.power, wp.age)
3. Now all we have to do is matching power, age and coins needed with the results we get from subquery. (and (w.power, wp.age, w.coins_needed) in)
*/


select  w.id, wp.age, w.coins_needed, w.power 
from wands w 
inner join wands_property wp on w.code = wp.code 
where wp.is_evil = 0 
and (w.power, wp.age, w.coins_needed) in (
  select w.power, wp.age, min(w.coins_needed) 
  from wands w 
  inner join wands_property wp on w.code = wp.code 
  where wp.is_evil = 0 
  group by w.power, wp.age
)
order by w.power desc, wp.age desc;