/*
order by the last 3 charachetrs in ascending order: substr(name,-3,3) asc
order by the id in ascending order: id asc
*/

select name from students where marks > 75 order by substr(name,-3,3) asc, id asc;