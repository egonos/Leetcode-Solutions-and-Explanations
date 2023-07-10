/*Intuition
Hi everyone. Let's go over the code together:

from prices p
inner join unitssold u on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id;
This is the modified table that we pick the values from. Merging is done based on

Matching the product_id's.
Finding the correct inteval found in prices table for each purchase date.
Finally we have to calculate the average prices. If we sum up the units sold and the price within the interval for all time time intervals then divide this valu into the total units sold we can accomplish this.

That's what we are doing in here

sum(p.price*u.units)/sum(u.units)
And that basically it. THe final code looks like this:

Final Code*/

select p.product_id, round(sum(p.price*u.units)/sum(u.units),2) as average_price from prices p
inner join unitssold u on u.product_id = p.product_id and u.purchase_date between p.start_date and p.end_date
group by p.product_id;