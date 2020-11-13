import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

# to update a single value we use the following structure:
c.execute("""UPDATE customers SET email = 'medeiroscwb'     
            WHERE rowid = '1' """)
#changes the datum inside column 'email' and line '1' to 'medeiroscwb'
#In the WHERE argument, you may determine a condition that aplies to multipler entries

tab_all = c.fetchall()

for line in tab_all:
    print(line)

print("Record(s) updated.")

conn.commit()