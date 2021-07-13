-- display the top 3 cities temperatures during July and August
-- ordered by temperature
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 7 or month = 8
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;

