-- List all records of the table second_table where name values are present
SELECT score, name FROM second_table
WHERE name <> ''
ORDER BY score DESC;
