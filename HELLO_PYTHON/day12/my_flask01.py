from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/para')
def para():
    menu = request.args.get('menu')
    print(menu)
    return 'PARA1' + menu

@app.route('/post',methods=['POST'])
def mypost():
    if request.method == 'POST' :
        menu = request.form['menu']
        return 'POST:' + menu
    
@app.route('/disfor')
def disfor():
    a = "잼버리"
    b = ["홍길동","전우치","이순신"]
    c = [
        {'e_id':'1','e_name':'1','gen':'1','addr':'1'},
        {'e_id':'2','e_name':'2','gen':'2','addr':'2'}
    ]
    return render_template('disfor.html', a=a, b=b, c=c)

# for k, v in some_dict.items() %}
# key: {{k}}, value:{{v}}
# <br/>
# {% endfor %}

@app.route('/emp')
def emp():

    conn = pymysql.connect(host='127.0.0.1',
                       port=3305, # port 3306 default 값이면 생략 가능
                       user='root',
                       password='python',
                       db='python',
                       charset='utf8')

    try :
        curs = conn.cursor(pymysql.cursors.DictCursor)
        sql = "SELECT * FROM emp"
        curs.execute(sql)
        emps = curs.fetchall()
        print(emps)
    finally:
        curs.close()
        conn.close()

    return render_template('emp.html', emps=emps)


if __name__ == '__main__':
  app.run(debug=True)