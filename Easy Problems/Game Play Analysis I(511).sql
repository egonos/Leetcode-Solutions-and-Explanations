/*
Intuition
Hi everyone. Lets go one by one:

select player_id, min(event_date)
The question requires us to return the first event_date for each player

as first_login from activity
The first event date should be named as first_login. The code above provides this.

group by player_id
To return first event_date for each player we need to group the event dates based on the player id's.

All in a whole looks like this:
*/

select player_id, min(event_date) as first_login from activity
group by player_id;