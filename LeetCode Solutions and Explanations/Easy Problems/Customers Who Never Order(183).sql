/*
Intuition
Hi everyone! The key aspect of this problem is to use left join when merging the tables. This way we can keep the people having no orders in the merged table.

Rest of the operations are conventional:

(1)
*/

c.name Customers 

/*
The output should be Customers

(2)
*/
c.id = o.customerId

/*
Id on the customer table should match with customerId on the orders table.

(3)
*/
where o.customerId is NULL

/*
Filter the names having null customerId (do not have any orders)

(4)

The final solution would be:
*/

select c.name Customers from
customers c left join orders o on c.id = o.customerId where o.customerId is NULL;