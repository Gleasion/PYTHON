import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()
    
    e_name = "5" 
    gen = "5"
    addr = "5"
    e_id = 3
    
    sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            WHERE
                e_id = {e_id}
            """
    
    curs.execute(sql)
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
finally:
    curs.close()
    conn.close()
