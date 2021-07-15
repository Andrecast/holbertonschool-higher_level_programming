-- 9. Cities by States
-- list all cities with his states contained in the DB hbtn_0d_usa
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states
ON cities.state_id = states.id
ORDER BY cities.id ASC;
