/*
We begin by extracting the year and month information from the trans_date column. To achieve this, we utilize the date_format function.

The columns we require include: country (for grouping purposes), transaction count, approved transaction count, the total transaction amount, and the total approved transaction amount. These are typically calculated only in the context of grouped queries. Besides country, we must also group by the year-month combination.

The sum and case functions are key in calculating the values we require. For counting transactions, we identify and count the occurrences where certain conditions are met. In contrast, for summing transaction amounts, we sum the transaction amounts where certain conditions are met.
Here is the final code:
*/


select date_format(trans_date, '%Y-%m') as month ,country,count(*) as trans_count, sum(case
                                                                                        when state = 'approved' then 1
                                                                                        else 0 end) as approved_count,sum(amount) as trans_total_amount, sum(case 
                                                        when state = 'approved' then amount
                                                        else 0 end) as approved_total_amount

from transactions group by month,country; 
