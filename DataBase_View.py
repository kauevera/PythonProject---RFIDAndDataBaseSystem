import pandas as pd
import sqlite3
import time

##Creating a view using "Pandas" library
while True:
    conn = sqlite3.connect("banco_db")

    cur = conn.cursor()

    df = pd.read_sql_query("SELECT ID, DIA_HORA, OBJECT_NUMBER, OBJECT_NAME, STATE FROM ESP", conn)
    conn.close()
    time.sleep(3)
    print(df)
