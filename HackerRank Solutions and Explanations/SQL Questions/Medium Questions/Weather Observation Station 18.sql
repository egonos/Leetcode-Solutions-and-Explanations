/*
Recall manthatten distance: |x1 - x2| + |y1 - y2|
*/

select round((max(long_w) - min(long_w) + max(lat_n) - min(lat_n)),4) from station;