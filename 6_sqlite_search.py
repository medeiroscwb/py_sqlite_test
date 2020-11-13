import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

##query the database, selecting entries from determined conditions
#c.execute("SELECT rowid, * FROM customers WHERE last_name = 'lavanholi'")  ##here 'lavanholi' was the argument to be searched for
#c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE 'lu%'")  ##here we will search for entries that start with 'lu', finding Zera and Auroque
c.execute("SELECT rowid, * FROM customers WHERE rowid >= 3")  ##here we will search for entries starting from rowid 3 (the 4th element)

tab_all = c.fetchall() ##

for line in tab_all:
    print(line)

print("Search completed.")

conn.commit()
