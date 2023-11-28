from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql
from flask.json import jsonify
from day17.daomem import DaoMem
app = Flask(__name__)
dm = DaoMem()

@app.route('/')
@app.route('/mem')
def emp():
    return render_template('mem.html')

@app.route('/mylist', methods=['POST'])
def mylist():
    list = dm.selectList()
    return jsonify({'list' : list})

@app.route('/myone', methods=['POST'])
def myone():
    m_id = request.form['m_id']
    mem = dm.selectOne(m_id)
    print('m_id', m_id)
    return jsonify({'mem': mem})

@app.route('/myadd', methods=['POST'])
def myadd():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    age = request.form['age']
    height = request.form['height']
    
    cnt = dm.insert(m_id, m_name, age, height)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

@app.route('/mymod', methods=['POST'])
def mymod():
    m_id = request.form['m_id']
    m_name = request.form['m_name']
    age = request.form['age']
    height = request.form['height']
    
    cnt = dm.update(m_id, m_name, age, height)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

@app.route('/mydel', methods=['POST'])
def mydel():
    m_id = request.form['m_id']
    print('m_id', m_id)
    
    cnt = dm.delete(m_id)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

if __name__ == '__main__':
  app.run(debug=True)