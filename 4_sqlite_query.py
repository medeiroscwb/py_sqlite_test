import sqlite3

conn = sqlite3.connect("customers.db")
c = conn.cursor()

##query the database
c.execute("SELECT * FROM customers")

#print(c.fetchone())     ##This one will print the first line of the table as a tuple
#print(c.fetchmany(2))  ##This one will print the first "2" lines of the table as tuples in a list
#print(c.fetchall())  ##this one will return all the lines as tuples in a list

##u can put a positional argument after the fetch command to fetch for an specific column from the line.

tab_all = c.fetchall()

"""
for line in tab_all:
    print(line)
"""
#prints:
#('Felipe', 'Medeiros', 'medeiroscwb@gmail.com')
#('luiz', 'lavanholi', 'auroque')
#('luis', 'cavalheiro', 'zera')
#('icaro', 'naser', 'metalicarus')

for line in tab_all:
    print(line[0] + "." + line[1]  + "\t" + "  " + line[2])



print("Query completed.")

conn.commit()
