import datetime
import sqlite3

##Function to update object state
def update_state(banco_db, tabela, item):
    conn = sqlite3.connect(banco_db)
    cur = conn.cursor()

    comando = ("UPDATE " + tabela + " SET STATE = not STATE where DADO_LIDO = ?")
    cur.execute(comando, (item,))

    conn.commit()
    conn.close()

##Function to check if the object exists whithin database.
def check_exi(banco_db, tabela, coluna, item):
    conn = sqlite3.connect(banco_db)
    cur = conn.cursor()

    comando = ("SELECT 1 FROM " + tabela + " WHERE " + coluna + " = ?")
    cur.execute(comando, (item,))

    result = bool(cur.fetchone())

    conn.close()

    return result
