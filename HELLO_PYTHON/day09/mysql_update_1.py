import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3305, # port 3306 default 값이면 생략 가능
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8')


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
    cnt = curs.execute(sql)
    conn.commit()
    
    print("cnt", cnt)
    
finally:
    curs.close()
    conn.close()
