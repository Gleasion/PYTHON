import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')

try :
    sql = "SELECT * FROM emp"
    curs = conn.cursor()
    curs.execute(sql)
    print(curs.fetchall())
finally:
    curs.close()
    conn.close()