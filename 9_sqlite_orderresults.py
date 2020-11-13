import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

#c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")   ##orders by rowid descending
c.execute("SELECT rowid, * FROM customers ORDER BY first_name")   ##orders alphabeticaly by first name

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Table Ordered.")

conn.commit()