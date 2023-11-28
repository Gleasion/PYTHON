import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()

    sql = "INSERT INTO emp (e_id, e_name, gen, addr) VALUES (:1, :2, :3, :4)"
    
    curs.execute(sql, (5,'5','5','5'))
    
    conn.commit()
    
finally:
    curs.close()
    conn.close()