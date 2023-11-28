import cx_Oracle
import datetime

def insert10man():
    conn = cx_Oracle.connect('python/python@localhost:1521/xe')

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

            curs.execute(sql)
            conn.commit()
            
            cnt = curs.rowcount
            
            print(i,cnt)
            
    
    finally:
        curs.close()
        conn.close()

bef = datetime.datetime.now()
insert10man()
aft = datetime.datetime.now()
ell = aft - bef
print(ell)