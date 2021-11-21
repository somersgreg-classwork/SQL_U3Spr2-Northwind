# Northwind.py sprint assignment

import sqlite3

# Connect to sqlite3 file and create cursor object
conn = sqlite3.connect("northwind_small.sqlite3")
curs = conn.cursor()

# Queries
# What are the ten most expensive items?
expensive_items = f"""
    SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;
    """
print("What are the ten most expensive items (per unit price) in the database? ",
      curs.execute(expensive_items).fetchall(),
      )

# What is the average hire age?
avg_hire_age = f"""
    SELECT avg(HireDate - Employee.BirthDate)AS average_age FROM Employee;
    """
print("What is the average age of an employee at the time of their hiring? ",
      curs.execute(avg_hire_age).fetchall()[0][0],
      )

# Avg age by city:
avg_age_by_city = f"""
    SELECT city, avg(HireDate - Employee.BirthDate) AS average_age FROM Employee GROUP BY City
    """
print("How does the average age of employee at hire vary by city? ",
      curs.execute(avg_age_by_city).fetchall(),
      )

# Joins

conn.commit()
conn.close()
