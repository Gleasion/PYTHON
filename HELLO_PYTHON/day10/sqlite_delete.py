import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    sql = "DELETE FROM mem WHERE m_id = ?"
    
    curs.execute(sql, (5,))
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
    
finally:
    curs.close()
    conn.close()