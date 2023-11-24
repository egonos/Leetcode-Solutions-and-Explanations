/*Intuition
The solution of this problem is not hard but tricky. How can we obtain the numbers with conscective occurances? If it does not have to be conscecutive then we could group the numbers and return the numbers having 3+ occurances. The solution lies on the ids. If

We merge the table with itself on id's while substracting one from id's each time (sliding the table)
Check whether the sliding id's correspond to the same number for three times
then it means we found the answer. THe related code is this:

Code*/

select distinct l1.num as ConsecutiveNums  from logs l1
inner join logs l2 on l1.id = l2.id-1
inner join logs l3 on l2.id = l3.id-1
where l1.num = l2.num and l2.num = l3.num;