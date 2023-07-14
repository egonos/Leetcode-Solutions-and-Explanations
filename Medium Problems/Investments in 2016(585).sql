/*Intuition
Hi everyone. This is my solution. Here is what it is doing:

1. Joins the table by itself. (We want to show different instances having same 2015 insurances on the same row.)
2. (i1.lat <> i2.lat) and (i1.lon <> i2.lon) allows us to make sure that the selected instances have unique (lat,lon) pairs.
3. Last row in whole filters the multiple occured 2016 insurance instances.
I hope it will be helpful.

Code
*/
select round(sum(distinct i1.tiv_2016),2) as tiv_2016 from insurance i1
inner join insurance i2 on i1.tiv_2015 = i2.tiv_2015
where (i1.lat <> i2.lat) and (i1.lon <> i2.lon) and 
i1.tiv_2016 in (select distinct tiv_2016 from insurance group by lat,lon having count(*) = 1);