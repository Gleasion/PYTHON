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
    sql = "UPDATE emp SET e_id = %s, e_name = %s, gen = %s, addr = %s WHERE e_id = %s"
    curs.execute(sql, (5,'5','5','5',3))
    conn.commit()
finally:
    curs.close()
    conn.close()
