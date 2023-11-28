import sqlite3
import datetime

def insert10man():
    conn = sqlite3.connect('python.db')

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
            cnt = curs.rowcount
            # conn.commit()
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