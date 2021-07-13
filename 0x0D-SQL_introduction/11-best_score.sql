-- list score and name, in this order
-- all the records with score >= 10 in descendant order
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;

