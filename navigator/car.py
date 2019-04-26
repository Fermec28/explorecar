#Model of simple car
class Car:
    @classmethod
    def foward(cls):
        print("move the car foward")

    @classmethod
    def rigth(cls):
         print("move the car on the rigth")

    @classmethod
    def left(cls):
         print("move the car on the left")

    @classmethod
    def reverse(cls):
         print("move the car on the reverse")

    @classmethod
    def stop(cls):
        print("stop the car")




Car.foward()
Car.rigth()
Car.left()
Car.reverse()
Car.stop()
