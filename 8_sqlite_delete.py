import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

c.execute("""DELETE from customers WHERE rowid = 2""") ##deletes the row 2

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Record(s) deleted.")

conn.commit()