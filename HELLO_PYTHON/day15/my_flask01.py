from flask import Flask
from flask.globals import request
from flask.templating import render_template
import pymysql
app = Flask(__name__)

@app.route('/')   
@app.route('/disfor')
def disfor():
    return render_template('disfor.html')

if __name__ == '__main__':
  app.run(debug=True)