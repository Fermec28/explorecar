from flask import Flask
from car import Car
app = Flask(__name__)


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

if __name__ == '__main__':
    app.run()
