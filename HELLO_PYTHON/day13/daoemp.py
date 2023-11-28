import pymysql

class DaoEmp :
    def __init__(self) :
        self.conn = pymysql.connect(host='127.0.0.1',
                       port=3305, # port 3306 default 값이면 생략 가능
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)

    def selectList(self):
        sql = "SELECT * FROM emp"
        self.curs.execute(sql)
        
        emp = self.curs.fetchall()
        return emp
    
    def selectOne(self, e_id):
        sql = f"SELECT * FROM emp WHERE e_id = {e_id}"
        
        self.curs.execute(sql)
        emp = self.curs.fetchall()
        return emp[0]

    def insert(self,e_id,e_name,gen,addr):
    
        sql = f"""
            INSERT INTO emp
            (e_id, e_name, gen, addr)
            VALUES ('{e_id}','{e_name}','{gen}','{addr}')
        """
    
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
        
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
    def update(self,e_id,e_name,gen,addr):
        sql = f"""
            UPDATE emp
            SET
                e_name = '{e_name}',
                gen = '{gen}',
                addr = '{addr}'
            WHERE
                e_id = {e_id}
            """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def delete(self,e_id):
        sql = f"""
        DELETE
        from emp
        WHERE
            e_id = '{e_id}'
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
if __name__ == '__main__':
    de = DaoEmp()
    # emp = de.selectList()
    # emp = de.selectOne(1)
    # emp = de.insert(4, '4', '4', '4')
    # emp = de.update(4, '6', '6', '6')
    # emp = de.delete(4)
    # print(emp)