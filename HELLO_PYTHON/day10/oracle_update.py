import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()

    sql = "UPDATE emp SET e_name = :1, gen = :2, addr = :3 WHERE e_id = :4"
    
    curs.execute(sql, ('1','1','1',5))
    
    conn.commit()
    
finally:
    curs.close()
    conn.close()