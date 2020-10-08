<details>
<summary>Table of Content</summary>

- [CS2208 Week 1](#cs2208-week-1)
  - [Module Content](#module-content)
  - [Databases (General)](#databases-general)
    - [Example: Online Bookseller](#example-online-bookseller)
      - [Using Databases](#using-databases)
    - [Database Management System](#database-management-system)
      - [What Functions should a DBMS provide](#what-functions-should-a-dbms-provide)
      - [DBMS Benefits](#dbms-benefits)
      - [Key Data Management Concepts](#key-data-management-concepts)
  - [Relational Databases](#relational-databases)
  - [Table Implementation](#table-implementation)
    - [Row Major Order](#row-major-order)
    - [Column Major Order](#column-major-order)
  - [SQL Examples](#sql-examples)
    - [Example: Selection Query](#example-selection-query)
      - [Base Table](#base-table)
      - [Query](#query)
      - [Output Table](#output-table)
    - [Example: Projection Query](#example-projection-query)
      - [Base Table](#base-table-1)
      - [Query](#query-1)
      - [Output Table](#output-table-1)
  - [SQL Query Functionality](#sql-query-functionality)
    - [Selections](#selections)
    - [Joins](#joins)
  - [SQL Keywords](#sql-keywords)
    - [Like](#like)
    - [Distinct](#distinct)
    - [Order By](#order-by)
  - [SQL Database Functionality](#sql-database-functionality)
    - [Selecting Data](#selecting-data)
    - [Updating Data](#updating-data)
    - [Inserting Data](#inserting-data)
    - [Deleting Data](#deleting-data)
  - [The MySQL Server](#the-mysql-server)
    - [Command Line Interface](#command-line-interface)
  - [Tables](#tables)
    - [Primary Key](#primary-key)
    - [Delete Primary Key](#delete-primary-key)
  - [Example: Quiz](#example-quiz)
    - [Quiz Database Structure](#quiz-database-structure)
      - [Quiz Table](#quiz-table)
      - [Question Table](#question-table)
      - [Answer Table](#answer-table)
    - [Quiz Database Schema](#quiz-database-schema)
  - [Further SQL Details](#further-sql-details)
    - [Null Values](#null-values)
    - [Aggregate Functions](#aggregate-functions)
      - [Example: Aggregate Function](#example-aggregate-function)
      - [Aggregate Functions - Group By](#aggregate-functions---group-by)
    - [Aggregate Functions (Cont.)](#aggregate-functions-cont)
      - [Aggregate Functions - Having Clause](#aggregate-functions---having-clause)
      - [Null Values and Aggregates](#null-values-and-aggregates)
      - [IN Operator](#in-operator)
      - [Exists Operator](#exists-operator)
      - [Nested Subqueries](#nested-subqueries)
    - [Modification of the Database](#modification-of-the-database)
      - [Deletion](#deletion)
      - [Insertion](#insertion)
      - [Updates](#updates)
      - [Destroying or Altering Relations](#destroying-or-altering-relations)
- [CS2208 Week 2](#cs2208-week-2)
  - [Relational Query Languages](#relational-query-languages)
    - [Formal Relational Query Languages](#formal-relational-query-languages)
    - [Preliminaries](#preliminaries)
    - [Relational Algebra](#relational-algebra)
      - [Projection](#projection)
      - [Selection](#selection)
      - [Union](#union)
        - [Implementation](#implementation)
      - [Intersection](#intersection)
      - [Set-Difference (Minus)](#set-difference-minus)
      - [Cross-Product (Times)](#cross-product-times)
    - [Joins](#joins-1)
      - [Nested Loop Joins](#nested-loop-joins)
      - [Natural Join](#natural-join)
    - [Relational Querys](#relational-querys)

</details>

---

# CS2208 Week 1

**Semester 1**: _Relational Databases_ using **SQL**<br>**Semester 2**: _Non-Relational Databases_ using **No-SQL**

## Module Content

- **Basic SQL**

  - Create **Tables**, basic **Joins**, **Primary Keys**, etc

- **Database Modelling**

  - Using **Entity Relationship Diagrams**, **Normal Forms**, **Relational Algebra/Calculus**

- **Advanced SQL**
  - Utilising **Indexing**, **Triggers**, etc

---

## Databases (General)

- What is a **Database**

  - A collection of files storing **Related Data**

- Example of **Databases**
  - Accounts Database
  - Payroll Database
  - UCC's Student Information Database
  - Amazon's Product Database
  - Airline Reservation Database

### Example: Online Bookseller

- What **Data Information** do we need

  - Data about Books, Customers, Pending Orders, Order History, Trends, Metrics, etc
  - Data about Web Sessions (Clicks, Page Views, Search History)

- What **Data Capabilities** do we need
  - Insert/Remove books, Find books by author/title/etc, Analyse past order history, Recommend books, etc
  - Data must be accessed **Efficiently** by many users
  - Data must be safe from **Failures** and **Malicious Users**
  - Data must be **Persistent**
    - Data will be very large
    - Data wont all fit in **Memory**

#### Using Databases

- Jane and John both have a shared **ID** number for a \$200 giftcard they got as a wedding gift

  - Jane while at her office orders a book - _"The Selfish Gene", \$80_
  - John while at his office orders a book - _"Guns of Steel", \$100_

- Reasons for **DBMS**
  - What is the ending credit left on the card?
  - What if the second book cost \$130?
  - What if the system crashes?

### Database Management System

- What is a **DBMS**

  - A big program written by someone else that allows us to **Efficiently** manage **Large Databases**
    and allows the database to persist over long periods of time

- Examples of **DBMS**
  - **Industry** - Oracle, IBM DB2, Microsoft SQL Server, etc
  - **Open Source** - MySQL, PostgreSQL, CouchDB
  - **Open Source Library** - SQLite

#### What Functions should a DBMS provide

- Describe real-world entities in terms of **Stored Data**
- **Persistently** store large **Datasets**
- Efficiently **Query** & **Update**
  - Must handle **Complex Questions** about the **Data**
  - Must handle **Sophisticated Updates**
  - **Performance** matters
- Change the **Data Structure** (add **Attributes**, etc)
- **Concurrency Control**
  - Enable **Simultaneous Updates**
- Crash **Recovery**
- **Security** and **Integrity**

#### DBMS Benefits

- It is **Expensive** to implement all these features inside an application without using a **DBMS**
- **DBMS** provides these features (and more)
- **DBMS** simplifies **Application Development**

#### Key Data Management Concepts

- **Data Models**
  - How to describe real-world **Data** using proper **Data Models**
    - e.g. **Relational**, **NoSQL**, etc
- **Declarative Query Languages**
  - Say _What_ you want **not** _How_ to get it
- **Data Independence**
  - **Physical** Independence
    - Able to change how **Data** is stored on **Disk** without needing to make changes to the applications
  - **Logical** Independence
    - Able to change **Database Schema** without affecting the applications
- **Query Optimizer**
  - Query plans and Understanding how they are executed
- **Physical Design**
- **Transactions**
  - **Isolation** and **Atomicity**

---

## Relational Databases

- Tables are not ordered
  - They are sets or multisets (bags)
- Tables are flat
  - Not nested attributes
- Tables do not prescribe how they are implemented/stored on the disk
  - This is called physical data independence

---

## Table Implementation

- How would you implement this?
  | cname | country | no_employees | for_profit |
  | :-------: | :-----: | :----------: | :--------: |
  | IBM | USA | 20000 | True |
  | Sony | Japan | 5000 | True |
  | Nintendo | Japan | 3000 | True |
  | AirCanada | Canada | 5000 | True |

  - 2D Array

### Row Major Order

```SQL
table=[
    ["IBM", "USA", 20000, "True"],
    ["Sony", "Japan", 5000, "True"],
    ["Nintendo", "Japan", 3000, "True"],
    ["AirCanada", "Canada", 5000, "True"]
    ]
```

- What **Operations** could we do **Efficiently** using a **Row Major Order**?

### Column Major Order

```SQL
table=[
    ["IBM", "Sonny", "Nintendo", "AirCanada"],
    ["USA", "Japan", "Japan", "Canada"],
    [20000, 5000, 3000, 5000],
    ["True", "True", "True", "True"]
    ]
```

- What **Operations** could we do **Efficiently** using a **Column Major Order**?

<br>

- What happens when you alter a **Table**?
- **Physical Data Independence**
  - Logical definition of the **Data** remains unchanged, even when we make changes to the actual **Implementation**

---

## SQL Examples

### Example: Selection Query

#### Base Table

|    PName    |  Price   |  Category   | Manufacturer |
| :---------: | :------: | :---------: | :----------: |
|    Gizmo    | \$19.99  |   Gadgets   |  GizmoWorks  |
| Powergizmo  | \$29.99  |   Gadgets   |  GizmoWorks  |
| SingleTouch | \$149.99 | Photography |    Canon     |
| MultiTouch  | \$203.99 |  Household  |   Hitachi    |

#### Query

```SQL
SELECT *
FROM Product
WHERE Category = "Gadgets"
```

#### Output Table

|   PName    |  Price  | Category | Manufacturer |
| :--------: | :-----: | :------: | :----------: |
|   Gizmo    | \$19.99 | Gadgets  |  GizmoWorks  |
| Powergizmo | \$29.99 | Gadgets  |  GizmoWorks  |

### Example: Projection Query

#### Base Table

|    PName    |  Price   |  Category   | Manufacturer |
| :---------: | :------: | :---------: | :----------: |
|    Gizmo    | \$19.99  |   Gadgets   |  GizmoWorks  |
| Powergizmo  | \$29.99  |   Gadgets   |  GizmoWorks  |
| SingleTouch | \$149.99 | Photography |    Canon     |
| MultiTouch  | \$203.99 |  Household  |   Hitachi    |

#### Query

```SQL
SELECT PName, Price, Manufacturer
FROM Product
WHERE Category = "Gadgets"
```

#### Output Table

|   PName    |  Price  | Category | Manufacturer |
| :--------: | :-----: | :------: | :----------: |
|   Gizmo    | \$19.99 | Gadgets  |  GizmoWorks  |
| Powergizmo | \$29.99 | Gadgets  |  GizmoWorks  |

---

## SQL Query Functionality

### Selections

```SQL

SELECT * FROM Product WHERE Price > 100.0
```

### Joins

```SQL
SELECT pname, price
FROM Product, Company
WHERE manufacturer = cname AND country="Japan" AND price < 150
```

---

## SQL Keywords

### Like

```SQL
SELECT *
FROM Products
WHERE PName LIKE "%gizmo%"
```

- Basic string pattern matching
  - X **LIKE** Y
  - Y may contain special symbols
    - **%** - Any sequence of characters

### Distinct

```SQL
SELECT DISTINCT Category
FROM Product
```

- Eliminate duplicates in the output

### Order By

```SQL
SELECT PName, Price, Manufacturer
FROM Product
WHERE Category = "gizmo" AND Price > 50
ORDER BY Price, PName
```

- Sorting Results
  - Ties get broken based on the second attribute of the **ORDER BY** statement
  - Orders in Ascending by default, Use **DESC** keyword to order in Descending

---

## SQL Database Functionality

### Selecting Data

```SQL
SELECT list_of_fields
FROM list_of_tables
WHERE where_clause
GROUP BY group_by_clause
HAVING having_clause
ORDER BY order_by_clause
```

- The **SELECT** statement is used to retrieve data from one or more databases

### Updating Data

```SQL
UPDATE Customers
SET ContactName = 'Maria Anderson'
WHERE CustomerId = 'ALFKI'
```

- The **UPDATE** statement is used to update information in database tables

### Inserting Data

```SQL
INSERT INTO [OrderDetails]
(OrderId, ProductId, UnitPrice, Quantity, Discount)
VALUES (10248, 2, 19.00, 2, 0)
```

- The **INSERT** statement is used to add one or more rows to a database table

### Deleting Data

```SQL
DELETE FROM Customers
WHERE CustomerId = 'ALFKI'
```

- The **DELETE** statement is used to remove information from database tables

---

## The MySQL Server

- A **MySQL** server can be given SQL commands, executes them, and results the results to the connected application
- Check student email for ucc database credentials

### Command Line Interface

- Used to start the **MySQL** client
- Commands for looking around in the database
  - **SHOW DATABASES**
  - **USE** database
  - **SHOW TABLES**

---

## Tables

- A typical database definition has:

  - Name
  - List of columns and their data types
  - List of constraints
    - Primary Key to ensure data uniqueness (if needed)
    - Foreign Keys
    - Indeices to facilitate fast look ups

### Primary Key

- The **primary key** is a field in a table which uniquely identifies each row/record in a database table
- **Primary keys** must contain **unique** values
- A **primary key** column cannot have **NULL** values
- A table can have only one **primary key**

  - May consist of a single field or multiple fields

- **Primary Keys** can be added after table has been created but its recommended to have your database structure planned out beforehand

**Primary Key** at table creation:

```SQL
CREATE TABLE Customers (
ID INT NOT NULL,
NAME VARCHAR (20) NOT NULL,
AGE INT NOT NULL,
ADDRESS CHAR (25) ,
SALARY DECIMAL (18, 2),
PRIMARY KEY (ID, NAME)
);
```

Adding **Primary Key** post table creation:

```SQL
ALTER TABLE Customers
ADD PRIMARY KEY (ID, NAME);
```

### Delete Primary Key

```SQL
ALTER TABLE Customers
DROP PRIMARY KEY;
```

- You can clear the **primary key** constraints from the table with this syntax

---

## Example: Quiz

### Quiz Database Structure

#### Quiz Table

| id  | description |  creation_date   |
| :-: | :---------: | :--------------: |
|  1  | Trivia Quiz | 10/07/2018 10:22 |

#### Question Table

| id  |               text               | quiz_id |
| :-: | :------------------------------: | :-----: |
|  1  | Who is the president of Ireland? |    1    |
|  2  | Who is the president of America  |    1    |
| ... |               ...                |   ...   |

#### Answer Table

| id  |       text        | point_value | question_id |
| :-: | :---------------: | :---------: | :---------: |
|  1  | Michael D Higgins |      1      |      1      |
|  2  |   Donald Trump    |     10      |      1      |
| ... |        ...        |     ...     |     ...     |

### Quiz Database Schema

```SQL
CREATE TABLE quiz (
id INT NOT NULL AUTO_INCREMENT,
description VARCHAR(255),
create_time DATETIME NOT NULL,
PRIMARY KEY(id)
)
```

```SQL
CREATE TABLE question (
id INT NOT NULL AUTO_INCREMENT,
text VARCHAR(255),
quiz_id INT NOT NULL,
PRIMARY KEY (id),
FOREIGN KEY (quiz_id) REFERENCES
quiz(id) ON DELETE CASCADE
)
```

```SQL
CREATE TABLE answer (
id INT NOT NULL AUTO_INCREMENT,
text VARCHAR(255) NOT NULL,
point_value INT NOT NULL,
question_id INT NOT NULL,
PRIMARY KEY(id),
FOREIGN KEY (question_id) REFERENCES
question(id) ON DELETE CASCADE
)
```

---

## Further SQL Details

- Data Types
  - Numbers: **INT**, **LONGINT**, **NUMBERIC**, **FLOAT**, **DOUBLE**
  - Strings: **VARCHAR**(NUM CHARS), **TEXT**, **BLOB**
  - Other: **DATETIME**
- **NOT NULL** vs **NULL**
  - Whether its allowed to have empty values or not
- **PRIMARY KEY** and **FOREIGN KEY**
- **CASCADE**
  - Keeping the data clean and robust

### Null Values

- It is possible for tuples to have **null** values, denoted by **null**, for some of their attributes
- **Null** signifies an unknown value or that a value does not exist
- The result of any arithmetic expression involving **null** is **null**
  - e.g. 5 + **null** equals **null**
- The predicate is **null** can be used to check for **null** values
  - **SELECT** name **FROM** instructor **WHERE** salary **is null**
- The predicate **null** is not **null** success if the value on which it is applied is not **null**
  <br>

- **SQL** treats as unknown the result of any comparison involving a **null** value (other than predicates is **null** and is not **null**)
  - e.g. 5 < **null** or **null** <> **null** or **null** = **null**
- The predicate in a where clause can involve Boolean operations (**and**, **or**, **not**); thus the definitions of the Boolean operations need to be extended to deal with the value unknown - **and**
  (true and unknown) = unknown,
  (false and unknown) = false,
  (unknown and unknown) = unknown - **or**
  (unknown or true) = true,
  (unknown or false) = unknown
  (unknown or unknown) = unknown
- Result of where clause predicate is treated as false if it evaluates to unknown
  <br>

### Aggregate Functions

- These functions operate on the multiset of values of a column of a relation, and return a value
  - **avg** - average value
  - **min** - minimum value
  - **max** - maximum value
  - **sum** - sum of values
  - **count** - number of values

#### Example: Aggregate Function

- Find the average salary of instructors in the Computer Science department

```SQL
SELECT AVG(salary) FROM instructor WHERE dept_name= 'Comp. Sci.'
```

- Find the total number of instructors who teach a course in the Spring 2010 semester

```SQL
SELECT COUNT (distinct ID) FROM teaches WHERE semester = 'Spring' and year = 2018
```

- Find the number of tuples in the course relation

```SQL
SELECT COUNT (*) FROM course;
```

#### Aggregate Functions - Group By

- Find the average salary of instructors in each department

```SQL
SELECT dept_name, AVG (salary) AS avg_salary FROM instructor
GROUP BY dept_name;
```

---

### Aggregate Functions (Cont.)

Attributes in select clause outside of aggregate functions must appear in group by list

**WRONG**

```SQL
SELECT dept_name, ID, AVG (salary)
FROM instructor
GROUP BY dept_name;
```

**CORRECT**

```SQL
SELECT dept_name, ID, AVG (salary)
FROM instructor
GROUP BY dept_name, ID;
```

#### Aggregate Functions - Having Clause

Find the names and average salaries of all departments whose average salary is greater than 42000

```SQL
SELECT dept_name, AVG (salary) AS avg_salary
FROM instructor
GROUP BY dept_name
HAVING AVG (salary) > 42000;
```

- **Note**: predicates in the having clause are applied after the formation of groups whereas predicates in the where clause are applied before forming groups
  <br>

#### Null Values and Aggregates

```SQL
SELECT SUM (salary ) FROM instructor
```

- Total all salaries
  - This statement ignores all **null** amounts
  - Result is null if there is no **non-null** amount
- All aggregate operations except **count**(\*) ignore tuples with null values on the aggregated attributes
- What if collection has only null values?
  - **count** returns 0
  - all other aggregates return **null**

#### IN Operator

- Shorthand for multiple **OR** conditions

```SQL
SELECT * FROM Customers
WHERE Country IN ('Germany', 'France', 'UK’);
```

- Selects all customers that are located in "Germany", "France" or "UK"

```SQL
SELECT * FROM Customers
WHERE Country NOT IN ('Germany', 'France', 'UK’);
```

- Selects all customers that are NOT located in "Germany", "France" or "UK"

#### Exists Operator

```SQL
SELECT column_name(s) FROM table_name
WHERE EXISTS
(SELECT column_name FROM table_name WHERE
condition);
```

- The **EXISTS** operator is used to test for the existence of any record in a subquery
- The **EXISTS** operator returns true if the subquery returns one or more records
- If a subquery returns any rows at all, **EXISTS** subquery is **TRUE**

**Exists**

```SQL
SELECT * FROM customers WHERE EXISTS
(SELECT * FROM orders WHERE
customers.customer_id = orders.customer_id);
```

- Find all records from the customers table where there is at least one record in the orders table with the same customer_id

**Not Exists**

```SQL
SELECT * FROM customers WHERE NOT EXISTS
(SELECT * FROM orders WHERE
customers.customer_id = orders.customer_id);
```

- **NOT** condition can be combined with the **EXISTS** condition to create a **NOT EXISTS** condition. Let's look at an example that shows how to use the **NOT EXISTS** condition in **SQL**

#### Nested Subqueries

- **SQL** provides a mechanism for the nesting of subqueries. A subquery is a selectfrom-where expression that is nested within another query

```SQL
SELECT A1, A2, ..., An FROM r1, r2, ..., rm WHERE P
```

- **From** clause: **ri** can be replaced by any valid subquery
- **Where** clause: **P** can be replaced with an expression
  - **B** <**operation**> (**subquery**)
    - Where **B** is an attribute and <**operation**> to be defined later
- **Select** clause - **Ai** can be replaced be a subquery that generates a single value

```SQL
SELECT * FROM Customers WHERE
Country IN (SELECT Country FROM Suppliers);
```

- Selects all customers that are from the same countries as the suppliers

---

### Modification of the Database

- Deletion of tuples from a given relation/table
- Insertion of new tuples into a given relation/table
- Updating of values in some tuples in a given relation/table

#### Deletion

```SQL
DELETE FROM instructor
```

- Delete all instructors

```SQL
DELETE FROM instructor
WHERE dept_name= 'Finance';
```

- Delete all instructors from the Finance department

```SQL
DELETE FROM instructor
WHERE salary < (SELECT AVG(salary)
FROM instructor);
```

- Delete all instructors whose salary is less than the average salary of instructors
  - **Problem** - as we delete tuples from deposit, the average salary changes
  - **Solution in SQL** 1. First, compute **avg** (salary) and find all tuples to delete 2. Delete all tuples found above (without recomputing **avg** or retesting the tuples)

#### Insertion

```SQL
INSERT INTO course
VALUES ('CS-437', 'Database Systems', 'Comp. Sci.', 4);
```

_or_

```SQL
INSERT INTO course (course_id, title, dept_name, credits)
VALUES ('CS-437', 'Database Systems', 'Comp. Sci.', 4);
```

- Add a new tuple to course

<br>

```SQL
INSERT INTO student
VALUES ('3003', 'Green', 'Finance', null);
```

- Add a new tuple to student with **tot_creds** set to **null**

<br>

```SQL
INSERT INTO instructor
SELECT ID, name, dept_name, 18000
FROM student
WHERE dept_name = 'Music' and total_cred > 144;
```

- Make each student in the Music department who has earned more than 144 credit hours an instructor in the Music department with a salary of \$18,000
- The select from where statement is evaluated fully before any of its results are inserted into the relation

```SQL
INSERT INTO table1 SELECT * FROM table1
```

- Otherwise queries like this would cause problems

#### Updates

```SQL
UPDATE instructor
SET salary = salary * 1.05
```

- Give a 5% salary raise to all instructors

```SQL
UPDATE instructor
SET salary = salary * 1.05
WHERE salary < 70000;
```

- Give a 5% salary raise to those instructors who earn less than 70000

```SQL
UPDATE instructor
SET salary = salary * 1.05
WHERE salary < (select avg (salary)
from instructor);
```

- Give a 5% salary raise to instructors whose salary is less than average

#### Destroying or Altering Relations

```SQL
DROP TABLE Students
```

- Destroys Students

```SQL
ALTER TABLE Students ADD COLUMN firstYear
```

- Students will be altered by adding a new field
- Every tuple in the current instance is extended with a null value in the new field

---

# CS2208 Week 2

## Relational Query Languages

- **Query Languages**
  - Allow manipulation and retrieval of **data** from a **database**
- **Relational** model supports **simple**, **powerful** QLs
  - Strong **formal foundation** based on logic
  - Allows for much **optimization**
- Query Languages **!=** Programming Languages
  - QLs not expected to be "Turing complete"
  - QLs not intended to be used for complex calculations
  - QLs support easy, efficient access to large data sets

### Formal Relational Query Languages

- Two mathematical Query Languages form the basis for “real” languages (e.g. SQL), and for implementation
  - **Relational Algebra**
    - More operational, very useful for representing execution plans
  - **Relational Calculus**
    - Lets users describe what they want, rather than how to compute it
      - Non-operational, declarative

### Preliminaries

- A query is applied to relation instances, and the result of a query is also a relation instance
  - Schemas of input relations for a query are fixed(but query will run regardless of instance)
  - The schema for the result of a given query is also fixed, Determined by definition of query language constructs
- Positional vs. Named-field Notation
  - Positional notation easier for formal definitions, named-field notation more readable
  - Both used in Relational Algebra and SQL

### Relational Algebra

- Basic operations
  - Selection ($\sigma$) - Selects a subset of rows from relation
  - Projection ($\pi$) - Deletes unwanted columns from relation
  - Cross-product ($X$) - Allows us to combine two relations
  - Set-difference ($-$) - Tuples in rel.1, but not in rel.2
  - Union ($\smile$) - Tuples in rel.1 and in rel.2
  - Renaming (for named perspective)
- Additional operations
  - Not essential, but very useful
    - Intersection
    - Join
    - Division
    - Renaming
- Since each operation returns a relation, operations can be composed

#### Projection

- Deletes attributes that are not in **projection list**
- **Schema** of result contains exactly the fields in the **projection list**, with the same names that they had in the (only) input relation
- Projection operator has to eliminate **duplicates**
  - **Note**: Real systems typically don’t do duplicate elimination unless the user explicitly asks for it
- $\pi$<sub> sname, rating</sub>S2

#### Selection

- Selects rows that satisfy **selection condition**
- **No duplicates** in result
- **Schema** of result identical to schema of (only) input relation
- **_Result_** relation can be the input for another **relational algebra operation** (Operator composition)
- $\pi$<sub>sname, rating</sub>($\sigma$<sub>rating>8</sub>(S2))

#### Union

- Produces a resulting relation that contains a tuple for every tuple in either or both of two input relations (duplicates only occur once)
- All of these operations take two input relations, which must be **compatible** (type-compatible)
  - Same number of fields
  - "Corresponding" fields have the same type
- S1$\smile$S2$\implies$sid, sname, rating, age

##### Implementation

- i=0
- j=0
- if T1[i] < T2[j]
  - print T1[i]
  - i+=1
- elif T1[i] > T2[j]
  - print T2[j]
  - j+=1
- elif both are the same
  - print any of them
  - increment both I and j
- print the remaining elements of the larger array

#### Intersection

- Produces a resulting relation that contains a tuple for every tuple in **BOTH** of the two input relations
- The relations being combined must be **compatible** (type-compatible)
- S1$-$S2$\implies$sid, sname, rating, age

#### Set-Difference (Minus)

- Produces a resulting relation that contains a tuple for every tuple in the first of two input relations and not in the second
- The Relations being combined must be **compatible** (type-compatible)

#### Cross-Product (Times)

**S1**
| sid | sname | rating | age |
|:---:|:-----:|:------:|:----:|
| 22 | dusty | 7 | 45.0 |
| 31 | lubby | 8 | 55.5 |
| 58 | rusty | 10 | 35.0 |

**S2**
| sid | sname | rating | age |
|:---:|:-----:|:------:|:----:|
| 28 | yuppy | 9 | 35.0 |
| 31 | lubby | 8 | 55.5 |
| 44 | guppy | 5 | 35.0 |
| 58 | rusty | 10 | 35.0 |

- Each row of S1 is paired with each row of R1
- Result schema has one field per field of S1 and R1, with field names "inherited" if possible
  - **Conflict**: Both S1 and R1 have a field called sid

### Joins

- **Conditional Join**:

  - R$\bowtie$<sub>$c$</sub>S = $\sigma$<sub>$c$</sub>(R$\times$S)
  - **Result schema** same as that of cross-product
  - Fewer tuples than cross-product, might be able to compute more efficiently
  - Sometimes called a **theta-join**

- **Equi-Join**:

  - A special case of condition join where the condition _c_ contains only equalities and ^
  - **Result schema** similar to cross-product, but only one copy of fields for which equality is specified
  - **Natural Join**: Equijoin on _all_ common fields

#### Nested Loop Joins

- Tuple-based nested loop R$\bowtie$S
- For each tuple r in R do
  - For each tuple s in S do
    - if r and s join then output (r,s)
- Cost: T(R) \* T(S)

#### Natural Join

- R1$\bowtie$R2 = $\Pi$<sub>A, B, ...</sub>($\sigma$<sub>s</sub>(R1$\times$R2))
- Where
  - The selection s checks equality of all common attributes
  - The projection eliminates the duplicate common attributes

### Relational Querys

- **DB Example**
  <!-- - TODO: Check slide -->

  {

  }
