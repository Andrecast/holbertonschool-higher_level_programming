-- 5. Unique ID
-- creates the table unique_id on the MySQL server
CREATES TABLE IF NOT EXISTS unique_id (id INT NOT NULL DEFAULT 1 UNIQUE,
name VARCHAR(256));

