import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    sql = "SELECT * FROM mem"
    
    curs.execute(sql)
    
    mList = []
    
    rows = curs.fetchall()
    
    for r in rows:
        mList.append({'m_id':r[0],'m_name':r[1],'tel':r[2],'addr':r[3]})
    
    print(mList)
finally:
    curs.close()
    conn.close()