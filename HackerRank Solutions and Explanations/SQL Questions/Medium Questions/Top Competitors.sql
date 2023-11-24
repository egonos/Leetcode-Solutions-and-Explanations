/*
Explanation
We need to join all the tables togatherutilizing th common columns
Then we need to group by the hacker_id and name (Since we will use a count operation)
Then we need to filter the results by the count of the challenge_id (Question statement says that the hacker should have submitted more than 1 challenge)
Then we need to order by the count of the challenge_id and the hacker_id

The link I got help from: https://github.com/tamirlan1/HackerRank/blob/master/SQL/TheCompetitiors.sql
*/

select s.hacker_id,h.name from
submissions s
inner join hackers h on s.hacker_id = h.hacker_id
inner join challenges c on s.challenge_id = c.challenge_id
inner join difficulty d on d.difficulty_level = c.difficulty_level
where d.score = s.score
group by h.name, h.hacker_id
having count(s.challenge_id) > 1
order by count(s.challenge_id) desc,
h.hacker_id asc;