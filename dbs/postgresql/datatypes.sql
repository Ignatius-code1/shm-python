
-- FIRST COLUMN -> unique
--sql SQL SYNTAX variable in small
-- SERIAL ->
-- UUID ->random 16 or 18 
-- random 
CREATE TABLE IF NOT EXISTS student(
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    dob DATE,
    phone INTEGER,
    marks REAL,
    another TEXT,
    is_married BOOLEAN,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO student (name,email,dob,phone,marks)
VALUES ('alice','alice@gmail.com','Hellow eorld',254732323,88.2);

-- SELECT * FROM student