# Write your MySQL query statement below
SELECT Email from Person
group by email
HAVING count(*) >1;
