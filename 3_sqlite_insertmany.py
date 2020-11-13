import sqlite3

conn = sqlite3.connect("customers.db")

c = conn.cursor()

many_custumers =[("luiz","lavanholi","auroque"),
                 ("luis","cavalheiro","zera"),
                 ("icaro","naser","metalicarus")]  ##put the data you want to input in the table as tuples in a list.

c.executemany("INSERT INTO customers VALUES(?,?,?)",many_custumers)  ##this command will insert the tuoles from list as lines in the table

print("INSERT_MANY Executed")

conn.commit()

