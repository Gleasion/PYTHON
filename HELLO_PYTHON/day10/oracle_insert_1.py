import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()
    
    e_id = 5
    e_name = "5"
    gen = "5"
    addr = "5"
    
    sql = f"""
        INSERT INTO emp
        (e_id, e_name, gen, addr)
        VALUES ('{e_id}','{e_name}','{gen}','{addr}')
    """
    
    curs.execute(sql)
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
finally:
    curs.close()
    conn.close()
