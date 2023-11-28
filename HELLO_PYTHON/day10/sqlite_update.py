import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    sql = "UPDATE mem SET m_name = ?, tel = ?, address = ? WHERE m_id = ?;"
    
    curs.execute(sql, ('5','5','5', 3))
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
    
finally:
    curs.close()
    conn.close()