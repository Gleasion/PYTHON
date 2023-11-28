from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql
app = Flask(__name__)

@app.route('/')
@app.route('/ttt')
def ttt():
    return render_template('ttt.html')

@app.route('/ttt01')
def ttt01():
    return render_template('ttt01.html')

if __name__ == '__main__':
  app.run(debug=True)