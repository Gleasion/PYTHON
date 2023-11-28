import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    curs = conn.cursor()
    
    e_id = 3
    
    sql = f"""
        DELETE
        from emp
        WHERE
            e_id = '{e_id}'
    """
    
    curs.execute(sql)
    
    cnt = curs.rowcount
    
    conn.commit()
    
    print("cnt",cnt)
finally:
    curs.close()
    conn.close()
