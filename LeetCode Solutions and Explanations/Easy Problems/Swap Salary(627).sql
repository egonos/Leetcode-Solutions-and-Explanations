/*
Intuition
Hi everybody. For this problem we need to update the original table. For that purpose, we need to use update operator.

To change accordant to the question statement, we need to define the conditions beforehand. This is when case operator becomes handy:
*/

update salary
set sex = case
            when sex = 'm' then 'f'
            else 'm'
            end;