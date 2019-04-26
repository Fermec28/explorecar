#import RPi.GPIO as GPIO
# lets us have a delay
from time import sleep

wheel1_0 = 24
wheel1_1 = 24
wheel2_0 = 24
wheel2_1 = 24
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(24, wheel1_0) #0 wheel 1
#GPIO.setup(24, wheel1_1) #1 wheel 1
#GPIO.setup(24, wheel2_0) #0 wheel 2
#GPIO.setup(24, wheel2_1) #1 wheel 2
#Model of simple car
class Car:
    @classmethod
    def foward(cls):
        #set the ports correctly
        #GPIO.output(wheel1_0, 1)
        #GPIO.output(wheel1_1, 0)
        #GPIO.output(wheel2_0, 1)
        #GPIO.output(wheel2_1, 0)

        sleep(.30)
        print("move the car foward")
        cls.stop()

    @classmethod
    def rigth(cls):
        #set the ports correctly
        #GPIO.output(wheel1_0, 0)
        #GPIO.output(wheel1_1, 1)
        #GPIO.output(wheel2_0, 1)
        #GPIO.output(wheel2_1, 0)

        sleep(.30)
        print("move the car on the rigth")
        cls.stop()

    @classmethod
    def left(cls):
        #set the ports correctly
        #GPIO.output(wheel1_0, 1)
        #GPIO.output(wheel1_1, 0)
        #GPIO.output(wheel2_0, 0)
        #GPIO.output(wheel2_1, 1)

        sleep(.30)
        print("move the car on the left")
        cls.stop()

    @classmethod
    def reverse(cls):
        #set the ports correctly
        #GPIO.output(wheel1_0, 0)
        #GPIO.output(wheel1_1, 1)
        #GPIO.output(wheel2_0, 0)
        #GPIO.output(wheel2_1, 1)

        sleep(.30)
        print("move the car on the reverse")
        cls.stop()

    @classmethod
    def stop(cls):
        print("stop the car")
        #GPIO.output(wheel1_0, 0)
        #GPIO.output(wheel1_1, 0)
        #GPIO.output(wheel2_0, 0)
        #GPIO.output(wheel2_1, 0)



Car.foward()
Car.rigth()
Car.left()
Car.reverse()
Car.stop()
