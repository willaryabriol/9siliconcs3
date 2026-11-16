'''
a. What is duck typing?
- Duck typing is simply another way to achieve polymorphism apart from inheritance.
b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
- The Car class simply needs the method "speak" so it could work even if it does not inherit from Animal.
'''

class Car:
    def move():
        print("The car drives on the road.")

class Boat:
    def move():
        print("The boat sails on water.")

class Drone:
    def move():
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car1 = Car
boat1 = Boat
drone1 = Drone

start_trip(car1)
start_trip(boat1)
start_trip(drone1)

'''
How does the code demonstrate polymorphism?
- Each object has the same method name and method attributes. Polymorphism is having the exact same method name and attributes but the methods may function differently. The code demonstrates that objects can have the same methods but the methods do different stuff.
'''