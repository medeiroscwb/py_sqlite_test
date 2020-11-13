import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

c.execute("DROP TABLE customers")

conn.commit()

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Table droped.")

