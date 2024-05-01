import sqlite3
##Database creation

conn = sqlite3.connect("banco_db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS ESP (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL , DIA_HORA TEXT NOT NULL, DATA_READ TEXT NOT NULL, OBJECT_NUMBER INTEGER NOT NULL, OBJECT_NAME TEXT, STATE BOOL NOT NULL)")

conn.commit()

conn.close()
