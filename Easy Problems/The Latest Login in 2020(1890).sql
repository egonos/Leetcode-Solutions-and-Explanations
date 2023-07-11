/*Intuition
Hi everyone. In my solution I've done the following:

Filter the time_stamps using first days of 2020 &2021.
Grouped rest of the data by user_id.
Only picked the maximum (lastest) date for each user_id.
All in whole it looks like this:

Code*/

select user_id, max(time_stamp) as last_stamp from logins 
where time_stamp >= '2020-01-01' and time_stamp < '2021-01-01'
group by user_id;