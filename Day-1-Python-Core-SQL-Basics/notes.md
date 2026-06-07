Day 1 Notes
Variables

Variables are used to store data in a program. They act like containers that hold values such as numbers, text, or other types of information. Variables make it easier to work with data and reuse it throughout the program.

Example:

name = "SomShekar"
age = 21
Loops

Loops are used to execute a block of code repeatedly until a specific condition is met. They help reduce code duplication and make programs more efficient when performing repetitive tasks.

Types of Loops
for loop – Used when the number of iterations is known.
while loop – Used when the number of iterations is not known in advance.

Example:

for i in range(5):
    print(i)
Lists

A list is a collection of multiple items stored in a single variable. Lists are ordered, mutable, and allow duplicate values. They are commonly used to store and process groups of related data.

Example:

numbers = [10, 20, 30, 40]

Common operations:

Adding elements using append()
Removing elements using remove()
Accessing elements using indexing
Dictionaries

A dictionary stores data in the form of key-value pairs. Each key is unique and is used to access its corresponding value. Dictionaries are useful when data needs to be organized and retrieved efficiently.

Example:

student = {
    "name": "SomShekar",
    "age": 21,
    "branch": "CSE"
}

Benefits:

Fast data lookup
Organized storage of related information
Easy access using keys
SELECT

The SELECT statement is used to retrieve data from a database table. It is one of the most frequently used SQL commands.

Example:

SELECT * FROM Student;

This query retrieves all records from the Student table.

WHERE

The WHERE clause is used to filter records based on a specific condition. It helps retrieve only the required data instead of the entire table.

Example:

SELECT * FROM Student
WHERE marks > 80;

This query displays students who scored more than 80 marks.

ORDER BY

The ORDER BY clause is used to sort data in ascending or descending order.

Example:

SELECT * FROM Student
ORDER BY marks DESC;

This query displays students sorted from highest marks to lowest marks.

Keywords:

ASC → Ascending order (default)
DESC → Descending order
LIMIT

The LIMIT clause is used to restrict the number of records returned by a query. It is useful when only a specific number of results are needed.

Example:

SELECT * FROM Student
LIMIT 5;

This query retrieves only the first 5 records from the Student table.