/*Intuition
Hi everyone. To calculate bonus correctly I've used case in my code.

If

a name does not start with 'M'
the employee_id is odd,
then the value is salary itself (bonus is 100%)
else the bonus is 0.

Code*/

select employee_id, case
                      when employee_id % 2 = 1 and substr(name,1,1) <> 'M' then salary
                      else 0
                      end

 as bonus from employees
 order by employee_id;