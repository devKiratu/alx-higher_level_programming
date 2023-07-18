-- This script lists all records of the table second_table of the database hbtn_0c_0 in your MySQL server.
-- It excludes records without a name and sorts the results by score (desc)
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
