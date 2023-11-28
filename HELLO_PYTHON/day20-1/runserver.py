from flask import Flask, jsonify, render_template
from subprocess import call
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.secret_key = "mysecret"

socket_io = SocketIO(app)

@app.route('/')
def hello_world():
    return "Hello Gaemigo Project Home Page!!"

@app.route('/chat')
def chatting():
    return render_template('chat.html')

@socket_io.on("message")
def handle_message(message):
    print("message : " + message)
    if message == 'new_connect':
        socket_io.emit('connect_message', "새로운 유저가 난입하였다!!") # emit 사용
    else:
        to_client = {'message': message, 'type': 'normal'}
        socket_io.emit('normal_message', to_client) # emit 사용

if __name__ == '__main__':
    socket_io.run(app, debug=True, port=9999)