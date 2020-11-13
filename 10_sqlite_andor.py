import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

#c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'lu%' OR rowid = 1 ")  ##sets a logic gate 'OR' and 2 conditions to fill the search
c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'lu%' AND rowid = 1 ")  ##sets a logic gate 'AND' and 2 conditions to fill the search

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Search completed.")

conn.commit()
