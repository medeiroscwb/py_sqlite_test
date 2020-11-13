import sqlite3

conn = sqlite3.connect("customers.db")

c = conn.cursor()

c.execute("""INSERT INTO customers VALUES("Felipe","Medeiros","medeiroscwb@gmail.com")""")  ##inserts a line in the table inside the db

print("INSERT_LINE Executed")

conn.commit()
