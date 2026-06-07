create database Student;
use Student;
CREATE TABLE Student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    department VARCHAR(50),
    marks INT
);

INSERT INTO Student VALUES
(1,'Ram',20,'CSE',85),
(2,'Anjali',21,'ISE',92),
(3,'Kiran',20,'ECE',78),
(4,'Priya',22,'CSE',88),
(5,'Arjun',21,'ISE',95);