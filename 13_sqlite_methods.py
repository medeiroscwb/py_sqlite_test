import sqlite3


db_name = 'customers'
tab_name = 'customers'


def gen_table():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("""CREATE TABLE {} (
        first_name text,                         
        last_name text,
        email text
        )""".format('tab_name'))
    print("Table Created")
    conn.commit()
    conn.close()


def insert_row():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute(
        """INSERT INTO {} VALUES("Felipe","Medeiros","medeiroscwb@gmail.com")""".format(tab_name))
    print("INSERT_LINE Executed")
    conn.commit()
    conn.close()


def insert_many():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    many_custumers = [("luiz", "lavanholi", "auroque"),
                      ("luis", "cavalheiro", "zera"),
                      ("icaro", "naser",
                       "metalicarus")]

    c.executemany("INSERT INTO customers VALUES(?,?,?)".format(), many_custumers)
    print("INSERT_MANY Executed")
    conn.commit()
    conn.close()


def query():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("SELECT * FROM {}".format(tab_name))
    tab_all = c.fetchall()
    for line in tab_all:
        print(line[0] + "." + line[1] + "\t" + "  " + line[2])
    print("Query completed.")
    conn.commit()
    conn.close()


def primary_key():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM {}".format(tab_name))
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Keys assigned.")
    conn.commit()
    conn.close()


def search():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE rowid >= 3")
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Search completed.")
    conn.commit()
    conn.close()


def update():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("""UPDATE customers SET email = 'medeiroscwb'     
                WHERE rowid = '1' """)
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Record(s) updated.")
    conn.commit()


def delete():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("""DELETE from customers WHERE rowid = 2""")
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Record(s) deleted.")
    conn.commit()
    conn.close()


def order_results():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers ORDER BY first_name")
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Table Ordered.")
    conn.commit()
    conn.close()


def and_or():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute(
        "SELECT rowid, * FROM customers WHERE first_name LIKE 'lu%' AND rowid = 1 ")
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Search completed.")
    conn.commit()
    conn.close()


def limiting():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC LIMIT 2 ")
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Search completed.")
    conn.commit()
    conn.close()


def droptable():
    conn = sqlite3.connect("{}.db".format(db_name))
    c = conn.cursor()
    c.execute("DROP TABLE customers")
    conn.commit()
    tab_all = c.fetchall()
    for line in tab_all:
        print(line)
    print("Table droped.")
    conn.close()