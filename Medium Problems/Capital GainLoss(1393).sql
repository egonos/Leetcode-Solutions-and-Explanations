/*
Hi everyone. Here is how I've solved this question.
We have to reassign the price values according to the Buy-Sell conditions.
For that purpose I've constructed anouther table with the stock_name and the net_price.
I've used the CASE statement to reassign the price values.
Then I've grouped the net_price values by stock_name and calculated the sum of the net_price values.
*/



select stock_name, sum(net_price) as capital_gain_loss from
(select stock_name, case
                        when operation = 'Buy' then -price
                        when operation = 'Sell' then price
                        end as net_price from stocks) as helper

group by stock_name;
                                 