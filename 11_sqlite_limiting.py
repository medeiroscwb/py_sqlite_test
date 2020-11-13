import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

#c.execute("SELECT rowid, * FROM customers LIMIT 2 ")  ##query the list but limit the results to 2
c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2 ")  ##U can use this to order from last to first

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Search completed.")

conn.commit()
