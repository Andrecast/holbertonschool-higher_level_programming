-- list the number of records with same score in second_table
-- displaying the score and the number of record with the label number
SELECT score, COUNT(score) as number
FROM second_table
GROUP BY score
ORDER BY score DESC;

