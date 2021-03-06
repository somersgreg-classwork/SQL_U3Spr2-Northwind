# -*- coding: utf-8 -*-
"""demo_data.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AlEI3XyoSxtd7PxtxgcgjRVegkOctmSe
"""

import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

query = f""" DROP TABLE IF EXISTS demo """

curs.execute(query)

# Create table

curs.executescript("""CREATE TABLE demo(s,x,y);""")

curs.executescript("""INSERT into demo(s,x,y)
              values('g',3,9),
              ('v',5,7),
              ('f',8,7);""")

row_count = curs.execute("SELECT COUNT(*) FROM demo")
print(f"How many rows are there?:",curs.fetchall())

xy_at_least_5 = f"""SELECT COUNT(*) FROM demo WHERE x >= 5 AND y >= 5"""
result = curs.execute(xy_at_least_5).fetchall()
print("How many rows where x and y are at least 5?:", result)

unique_y = curs.execute('SELECT COUNT(DISTINCT y) FROM demo').fetchall()
print(f"How many unique values of y are there?:",unique_y)

conn.commit()
curs.close