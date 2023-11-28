import sqlite3
from flask import Flask
from flask.globals import request
from flask.templating import render_template
from day14.daomem import DaoMem

app = Flask(__name__)
dm = DaoMem()

@app.route('/')
@app.route('/mem_list')
def mem():
    mList = dm.selectList()
    return render_template('mem_list.html',mList=mList)

@app.route('/mem_detail')
def mem_detail():
    m_id = request.args.get('m_id')
    mem = dm.selectOne(m_id)
    
    return render_template('mem_detail.html', mem=mem)

@app.route('/mem_insert')
def mem_insert():
    return render_template('mem_insert.html')

@app.route('/mem_insert_act', methods=['POST'])
def mem_insert_act():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    tel = request.form['tel']
    address = request.form['address']
    
    cnt = dm.insert(m_id, m_name, tel, address)
    
    return render_template('mem_insert_act.html', cnt=cnt)

@app.route('/mem_mod')
def mem_mod():
    m_id = request.args.get('m_id')
    mem = dm.selectOne(m_id)
    
    return render_template('mem_mod.html', mem=mem)

@app.route('/mem_mod_act', methods=['POST'])
def mem_mod_act():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    tel = request.form['tel']
    address = request.form['address']
    
    cnt = dm.update(m_id, m_name, tel, address)
    
    return render_template('mem_mod_act.html', cnt=cnt)

@app.route('/mem_del_act',methods=['POST'])
def mem_del_act():
    m_id = request.form['m_id']
    
    cnt = dm.delete(m_id)
    
    return render_template('mem_del_act.html', cnt=cnt)

if __name__ == '__main__':
    app.run(debug=True)
    

    
    
    
    