import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()

    sql = "DELETE from emp WHERE e_id = :1"
    
    curs.execute(sql, (5,))
    
    conn.commit()
    
finally:
    curs.close()
    conn.close()