# Navigator

This Directory contains the code to control a differential car, it works on
RaspberryPI


To run this code you must intall flask use pip install Flask
You have to install RPI.GPIO use pip install RPi.GPIO
You have to install correctly OPENCV

server.py is the server to listen the http request and socket events
camera.py abstraccion of camera with opencv
car.py abstraccion of car with RPi.GPIO
