from flask import Flask
from flask_socketio import SocketIO, send, emit
from car import Car
import base64
import cv2
camera = cv2.VideoCapture(0)  # init the camera 
app = Flask(__name__)
socketio = SocketIO(app, async_mode=None)

@app.route('/foward')
def foward():
    Car.foward()
    return "foward"

@app.route('/rigth')
def rigth():
    Car.rigth()
    return "foward"

@app.route('/left')
def left():
    Car.left()
    return "foward"

@app.route('/reverse')
def reverse():
    Car.reverse()
    return "foward"

@socketio.on('image')
def image():
    rabbed, frame = camera.read()  # grab the current frame
    #frame = cv2.resize(frame, (640, 480))  # resize the frame
    encoded, buffer = cv2.imencode('.jpg', frame)
    return base64.b64encode(buffer)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
