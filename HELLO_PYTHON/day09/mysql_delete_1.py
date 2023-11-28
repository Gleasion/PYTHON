# (cmd)창에서 입력하여 설치해야함
# conda install PyMySQL
# pip install pymySQL

import pymysql

conn = pymysql.connect(host='127.0.0.1',
                       port=3305, # port 3306 default 값이면 생략 가능
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8')


try :
    curs = conn.cursor()
    
    e_id = 3
    
    sql = f"""
        DELETE
        from emp
        WHERE
            e_id = '{e_id}'
    """
    cnt = curs.execute(sql)
    conn.commit()
    
    print("cnt", cnt)
finally:
    curs.close()
    conn.close()
