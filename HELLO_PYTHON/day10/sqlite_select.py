import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    sql = "SELECT * FROM mem"
    
    curs.execute(sql)
    print(curs.fetchall())
finally:
    curs.close()
    conn.close()