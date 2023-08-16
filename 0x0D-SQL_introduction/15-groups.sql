-- selects records with the same score
-- Select records

SELECT score, COUNT(`score`) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
