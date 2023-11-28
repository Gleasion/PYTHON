import sqlite3

class DaoMem:
    def __init__(self):
        self.conn = sqlite3.connect('python.db',check_same_thread=False)
        self.curs = self.conn.cursor()
        
    def selectList(self):
        sql = "SELECT * FROM mem"
        self.curs.execute(sql)
    
        mList = []
        rows = self.curs.fetchall()
    
        for r in rows:
            mList.append({'m_id':r[0],'m_name':r[1],'tel':r[2],'address':r[3]})
        
        return mList 
    
    def selectOne(self,m_id):
        sql = f"SELECT * FROM mem WHERE m_id = '{m_id}'"
        self.curs.execute(sql)
        
        mems = self.curs.fetchall()
        m = mems[0]
        return {'m_id':m[0],'m_name':m[1],'tel':m[2],'address':m[3]}
    
    def insert(self,m_id,m_name,tel,address):
        sql = f"""
            INSERT INTO MEM
            (m_id, m_name, tel, address)
            VALUES ('{m_id}','{m_name}','{tel}','{address}')
        """
        
        self.curs.execute(sql)
        cnt = self.curs.rowcount
        self.conn.commit()
        
        return cnt
    
    def update(self,m_id,m_name,tel,address):
        sql = f"""
            UPDATE MEM
            SET
                m_name = '{m_name}',
                tel = '{tel}',
                address = '{address}'
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
            from mem
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
    vo = dm.selectList()
    # vo = dm.selectOne(1)
    print(vo)
        
        
        
        
        
        