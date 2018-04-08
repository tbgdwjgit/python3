__author__ = 'Test-YLL'

import sqlite3

print(sqlite3.sqlite_version)

conn = sqlite3.connect('test.db')
print ("Opened database successfully")
c = conn.cursor()
# c.execute('''CREATE TABLE COMPANY
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        AGE            INT     NOT NULL,
#        ADDRESS        CHAR(50),
#        SALARY         REAL);''')
# print ("Table created successfully")

conn.commit()
conn.close()
print (c.rowcount)