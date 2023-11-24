/*
Explanation:

All we are doing is join all the tables based on company code then return the required information.

Why left join?
Because company_code may not be the same in all tables. So, we need to use left join to get all the data from company table.
If we use inner join, we will not get the companies that are not in the other tables.

distinct: To get the unique values.
*/

select
        c.company_code,
        c.founder,
        count(distinct lm.lead_manager_code),
        count(distinct sm.senior_manager_code),
        count(distinct m.manager_code),
        count(distinct e.employee_code)
        
from company c
left join
    lead_manager lm on lm.company_code = c.company_code

left join
    senior_manager sm on sm.company_code = lm.company_code
    
left join
    manager m on m.company_code = sm.company_code

left join 
    employee e on e.company_code = m.company_code

group by c.company_code,c.founder
order by c.company_code asc;
