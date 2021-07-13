-- list of records of second_table
-- don´t list rows without name value, display score and name
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

