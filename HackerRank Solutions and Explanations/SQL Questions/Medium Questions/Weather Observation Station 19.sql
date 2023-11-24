/*
Recall Euclidian distance: sqrt((x1 - x2)^2 + (y1 - y2)^2)

to get square root: SQRT()
to get square power: POW(...,2)
to get minimum: MIN()
to get maximum: MAX()
*/

select round(sqrt((pow(min(lat_n)- max(lat_n),2) + pow(min(long_w) - max(long_w),2))),4)from station;