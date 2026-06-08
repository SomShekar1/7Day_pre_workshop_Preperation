INSERT INTO Student VALUES
(1,'Ram',20,'CSE',85),
(2,'Anjali',21,'ISE',92),
(3,'Kiran',20,'ECE',78),
(4,'Priya',22,'CSE',88),
(5,'Arjun',21,'ISE',95);

SELECT * FROM Student;

SELECT name FROM Student;

SELECT name, marks FROM Student;


SELECT * FROM Student
WHERE department = 'CSE';


SELECT * FROM Student
WHERE marks > 80;


SELECT * FROM Student
WHERE age = 21;


SELECT * FROM Student
WHERE marks >= 90;


SELECT * FROM Student
ORDER BY marks ASC;


SELECT * FROM Student
ORDER BY marks DESC;


SELECT * FROM Student
ORDER BY name;


SELECT * FROM Student
LIMIT 3;


SELECT * FROM Student
ORDER BY marks DESC
LIMIT 1;


SELECT COUNT(*) FROM Student;


SELECT MAX(marks) FROM Student;


SELECT MIN(marks) FROM Student;


SELECT AVG(marks) FROM Student;


SELECT SUM(marks) FROM Student;


SELECT department,
COUNT(*)
FROM Student
GROUP BY department;


SELECT department,
AVG(marks)
FROM Student
GROUP BY department;


SELECT department,
AVG(marks)
FROM Student
GROUP BY department
HAVING AVG(marks) > 85;