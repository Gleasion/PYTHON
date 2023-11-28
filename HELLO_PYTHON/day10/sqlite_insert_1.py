import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    m_id = 15
    m_name = "3"
    tel = "3"
    address = "3"
    
    sql = f"""
        INSERT INTO mem
        (m_id, m_name, tel, address)
        VALUES
        ('{m_id}','{m_name}','{tel}','{address}')
    """
    
    curs.execute(sql)
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
finally:
    curs.close()
    conn.close()
