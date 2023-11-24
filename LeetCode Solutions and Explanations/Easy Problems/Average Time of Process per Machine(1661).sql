/*
Hi everyone! Here is my solution:
To calculate the average time of process per machine, we need to calculate the total time of each process and divide it into the number of processes per machine.
To calculate the total time I've used cte. In cte I've assign apprpriate sign for each timestamp (+<-end; -<-start))
After that I've sum up all the values and divide the result I get to number of different processes per machine.
In the end, I've rounded the result to 3 decimal places.
Here is the final code:
*/

with cte as
(select machine_id,process_id, case
                                when activity_type = 'start' then -timestamp
                                when activity_type = 'end' then timestamp
                                end as net_time from activity)

select machine_id, round(sum(net_time)/count(distinct process_id),3) as processing_time from cte
group by machine_id;
