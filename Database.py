import sqlite3

conn=sqlite3.connect("Mydatabase.db")

cursor=conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
               ID INTEGER PRIMARY KEY AUTOINCREMENT,
               NAME TEXT NOT NULL,
               AGE INTEGER NOT NULL)""")

conn.commit()

cursor.execute("INSERT INTO USERS(NAME,AGE) VALUES('MESSI',39)")
conn.commit()

cursor.execute("INSERT INTO USERS(NAME,AGE) VALUES('RONALDO',40)")
conn.commit()

cursor.execute("SELECT * FROM USERS")
for row in cursor.fetchall():
    print(row)

conn.close()