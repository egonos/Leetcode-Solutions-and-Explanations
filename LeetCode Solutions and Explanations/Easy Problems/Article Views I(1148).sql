/*Intuition
Hi everybody. For this problem, all we need to do is to select the necessary columns from the table(1), filter them by using where and sort them in ascending order by using order by. The final code looks like this:

Final Code*/

select distinct author_id as id from views
where author_id = viewer_id
order by author_id asc;