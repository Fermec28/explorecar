from flask import Flask
from flask_socketio import SocketIO, send, emit
from car import Car
from camera import Camera
import base64
import cv2

camera = Camera(0)
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
    return camera.get_image()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
