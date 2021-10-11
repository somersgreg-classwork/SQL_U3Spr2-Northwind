# SQL_U3Spr2-Northwind

Questions:

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

## In the Northwind database, what is the type of relationship between the Employee and Territory tables?
In the Northwind database, there is a many-to-many relationship between tables EmployeeTerritories, Employees, and Territories. An employee can be assigned to several territories, but these territories are not exclusive to an employee. Each employee can be linked to multiple territories, and each territory can be linked to multiple employees.

## What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?
If you are creating a project where the data is predictable, in terms of structure, size, and frequency of access, *relational* databases are the best choice.
If the data you are storing needs to be flexible in terms of shape or size, or if it needs to be open to change in future, then a *non-relational* database is the answer.

> "In a document database such as MongoDB the smallest unit is a document. In MongoDB, documents are stored in a collection, which in turn make up a database. Document are analogous to rows in a SQL table, but there is one big difference: not every document needs to have the same structure—each of them can have different fields and that is a very useful feature in many situations." (https://derickrethans.nl/introduction-to-document-databases.html)

## What is "NewSQL", and what is it trying to achieve?
NewSQL is a category of SQL database products that address the performance and scalability issues posed by traditional online transaction processing (OLTP) relational database management systems (RDBMS). 
Such systems aim to achieve the scalability of NoSQL systems while still providing the ACID attributes ensured by traditional relational databases. 
