import sqlite3

class DaoMem:
    def __init__(self):
        self.conn = sqlite3.connect('mem.db',check_same_thread=False)
        self.curs = self.conn.cursor()
        
    def selectList(self):
        sql = "SELECT * FROM member"
        self.curs.execute(sql)
    
        mList = []
        rows = self.curs.fetchall()
    
        for m in rows:
            mList.append({'m_id':m[0],'m_name':m[1],'age':m[2],'height':m[3]})
        
        return mList
     
    def selectOne(self,m_id):
        sql = f"SELECT * FROM MEMBER WHERE m_id = '{m_id}'"
        self.curs.execute(sql)
        
        mems = self.curs.fetchall()
        m = mems[0]
        
        return {'m_id':m[0],'m_name':m[1],'age':m[2],'height':m[3]}
    
    def insert(self,m_id,m_name,age,height):
        sql = f"""
            INSERT INTO MEMBER
            (m_id, m_name, age, height)
            VALUES ('{m_id}','{m_name}','{age}','{height}')
        """
        
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def update(self,m_id,m_name,age,height):
        sql = f"""
            UPDATE MEMBER
            SET
                m_name = '{m_name}',
                age = '{age}',
                height = '{height}'
            WHERE
                m_id = '{m_id}'
        """
        
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def delete(self,m_id):
        sql = f"""
            DELETE
            from MEMBER
            WHERE
                m_id = '{m_id}'
        """
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt

    def __del__(self):
        self.curs.close()
        self.conn.close()
    
if __name__ == '__main__':
    dm = DaoMem()
    list = dm.selectList()
    print(list)
    # cnt = dm.insert(2, 2, 2, 2)
    # cnt = dm.update(2, 3, 4, 5)
    # cnt = dm.delete(2)
    # print(cnt)
    # one = dm.selectOne(1)
    # print(one)
