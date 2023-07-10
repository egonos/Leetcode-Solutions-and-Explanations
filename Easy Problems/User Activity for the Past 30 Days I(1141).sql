/*Intuition
Hi everybody. Let's look at the code step by step:

select activity_date as day,count(distinct user_id) as active_users from activity
We are picking the necessary features from the original table.
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
This is a trick I've also recently learned. date_sub function is used for returning a previous date. We are using it to determine the start day. Using the obtained value, end date and between we can now write the required conditional statement. (We used 29 days because the end date is inclusive)

group by activity_date;
before counting the number of occurances, we need to state the groups. For this problem it should be activity_date.

Final Code*/

select activity_date as day,count(distinct user_id) as active_users from activity 
where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
group by activity_date;