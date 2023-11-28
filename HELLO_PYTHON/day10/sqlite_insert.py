import sqlite3

conn = sqlite3.connect('python.db')

try :
    curs = conn.cursor()
    
    sql = "INSERT INTO mem VALUES (?, ?, ?, ?);"
    
    cnt = curs.execute(sql, (10,'5','5','5'))
    
    conn.commit()
    
    print("cnt",cnt)
    
finally:
    curs.close()
    conn.close()