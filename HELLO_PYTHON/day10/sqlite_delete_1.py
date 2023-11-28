import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()

    m_id = 15
    
    sql = f"""
            DELETE FROM mem
            WHERE
                m_id = {m_id}
    """
    
    curs.execute(sql)
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt", cnt)
    
finally:
    curs.close()
    conn.close()