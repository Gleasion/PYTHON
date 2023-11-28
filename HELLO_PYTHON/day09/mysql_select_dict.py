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
    # python은 dictionary 라고 하는 것은
    # javascript의 json 형식과 같음
    curs = conn.cursor(pymysql.cursors.DictCursor)
    sql = "SELECT * FROM emp"
    curs.execute(sql)
    print(curs.fetchall())
finally:
    curs.close()
    conn.close()
