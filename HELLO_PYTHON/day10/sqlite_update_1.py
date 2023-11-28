import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    m_name = "11" 
    tel = "11"
    address = "11"
    m_id = 5
    
    sql = f"""
            UPDATE mem
            SET
                m_name = '{m_name}',
                tel = '{tel}',
                address = '{address}'
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