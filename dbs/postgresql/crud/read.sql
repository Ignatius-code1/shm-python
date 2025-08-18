
--SELECT <columns || *> 
--FROM <table> 
--WHERE <READ CONSTRAINS> 
--ORDER <> LIMIT <> 

--REad all columns and

--SELECT * FROM student;

--REad only name and email
-- SELECT name,email from student;

-- SELECT * from student
-- WHERE email='sam@gmail.com'
-- OR
-- email='alice@gmail.com'

-- SELECT * from student
-- WHERE pocket_money>50
-- AND pocket_money<100

SELECT * from student
ORDER BY name ASC
LIMIT 2