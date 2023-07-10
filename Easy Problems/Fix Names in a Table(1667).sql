/*Intuition
We need to make sure that

First letter is a capital letter
The rest of the letters are lowercase letters
We can do the first by using upper and substr(...,1,1)
We can do the second by using lower, substr(...,2, and now we have to find the length of the string so that we can substract 1 from it and give the resulting value to the substr. We can do it by using length command.
Finally we need to concatenate these two. concat is appropriate for this condition.
The final code looks like this:

Final Code*/

select user_id, concat(upper(substr(name,1,1)), lower(substr(name,2,length(name)-1))) as name from users
order by user_id;