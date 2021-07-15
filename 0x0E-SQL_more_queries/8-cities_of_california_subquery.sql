-- 8. Cities of California
-- list all the cities of California that can be found in the DB hbtn_0d_usa
SELECT id, name
FROM cities
WHERE state_id IN (
SELECT id
FROM states
WHERE name = 'California')
ORDER BY id ASC;

