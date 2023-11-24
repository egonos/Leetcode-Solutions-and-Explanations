/*Intuition
For this problem we need to do the following:

select the required column(s) and compute the necessary calculatons based on the information on the tables
Merge the reference columns by utilizing the common column (account in this case)
Group the data based on the account numbers because we want to learn the balance for each individual.
Only pick the ones having balance bigger than 10000.
The final code looks like this:

Code*/

select u.name,sum(t.amount) as balance from users u
inner join transactions t on u.account = t.account
group by u.account
having balance > 10000;