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

# c.execute('''INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (1, 'Paul', 32, 'California', 20000.00 )''');
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (2, 'Allen', 25, 'Texas', 15000.00 )");
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )");
# c.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

conn.commit()
conn.close()
print (c.rowcount)

