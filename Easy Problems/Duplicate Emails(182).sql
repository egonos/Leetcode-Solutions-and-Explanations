/*
Intuition
For this problem, our filter should based on the number of occurances for each email. For that purpose,
Select the email column (we'll return the duplicates)
Group them
Define the filter. having is the correct statement when we use aggregation.
*/

having count(*) > 1;

/*
means filter the nonduplicate emails.
The final code therefore;
*/

select email as Email from person 
group by email
having count(*) > 1;