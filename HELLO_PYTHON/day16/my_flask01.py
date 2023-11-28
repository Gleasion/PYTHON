from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql
from flask.json import jsonify
from day16.daoemp import DaoEmp
app = Flask(__name__)
de = DaoEmp()

@app.route('/')
@app.route('/emp')
def emp():
    return render_template('emp.html')

@app.route('/mylist', methods=['POST'])
def mylist():
    list = de.selectList()
    return jsonify({'list' : list})

@app.route('/myone', methods=['POST'])
def myone():
    e_id = request.form['e_id']
    emp = de.selectOne(e_id)
    print('e_id', e_id)
    return jsonify({'emp': emp})

@app.route('/mymod', methods=['POST'])
def mymod():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    cnt = de.update(e_id, e_name, gen, addr)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

@app.route('/myadd', methods=['POST'])
def myadd():
    e_id = request.form['e_id']
    e_name = request.form['e_name']
    gen = request.form['gen']
    addr = request.form['addr']
    
    cnt = de.insert(e_id, e_name, gen, addr)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

@app.route('/mydel', methods=['POST'])
def mydel():
    e_id = request.form['e_id']
    print('e_id', e_id)
    
    cnt = de.delete(e_id)
    
    print('cnt', cnt)
    return jsonify({'cnt': cnt})

if __name__ == '__main__':
  app.run(debug=True)