
-- FIRST COLUMN -> unique
--sql SQL SYNTAX variable in small
CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    dob TEXT,
    phone INTEGER,
    marks REAL
);

-- INSERT INTO student (name,email,dob,phone,marks)
-- VALUES ('alice','alice@gmail.com','2002-05-14',254732323,88.2);

-- SELECT * FROM student