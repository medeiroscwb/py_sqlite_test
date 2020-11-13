import sqlite3

conn = sqlite3.connect("customers.db")        ##u can name it :memory: to create a temporary db in memory

##cursor is the tool that modifies the database table, to create it:'''
c = conn.cursor()

##now we can create the table'''               ## ex: first name DATATYPE
c.execute("""CREATE TABLE customers (
    first_name text,                         
    last_name text,
    email text
    )""")
##this block will create a table with 3 columns within the database

#there are 5 possible datatypes:
#NULL
#INTEGER
#REAL
#TEXT
#BLOB


conn.commit()
##closes the connection
