import sqlite3

conn = sqlite3.connect("customers.db")

c = conn.cursor()

c.execute("SELECT rowid, * FROM customers")   ##This will just show the rowid. the rowid is native from the table and just numerate de rows top to bottom

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Keys assigned.")

conn.commit()
