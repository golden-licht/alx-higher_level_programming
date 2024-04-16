-- create a table second_table and add multiples rows

-- create the table if it doesn't exist already 
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(256),
    score INT
);

-- insert rows into the created table
INSERT INTO second_table 
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
