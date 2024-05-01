import sqlite3
conn = sqlite3.connect("banco_db")
cur = conn.cursor()

## Space to do changes of values inside the data base, only tests

##cur.execute("DELETE FROM ESP WHERE ID = 4")
##cur.execute("UPDATE ESP SET DADO_LIDO = 'OBJETO 2' WHERE (id =2)")
##cur.execute("ALTER TABLE `ESP` CHANGE `PATRIMONIO` `CODIGO PATRIMONIO` INTEGER NOT NULL")


conn.commit()

conn.close()
