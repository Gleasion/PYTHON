import pymysql
import datetime

def insert10man():
    conn = pymysql.connect(host='127.0.0.1',
                       port=3305, # port 3306 default 값이면 생략 가능
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8')

    try :
        curs = conn.cursor()
        
        for i in range(1,100000+1):
            col01 = i
            col02 = i%100
            
            sql = f"""
                INSERT INTO stress
                (col01, col02, col03, col04)
                VALUES ('{col01}','{col02}','{col02}','{col02}')
            """
            cnt = curs.execute(sql)
            #conn.commit()
            print(i,cnt)
        conn.commit()
    
    finally:
        curs.close()
        conn.close()

bef = datetime.datetime.now()
insert10man()
aft = datetime.datetime.now()
ell = aft - bef
print(ell)