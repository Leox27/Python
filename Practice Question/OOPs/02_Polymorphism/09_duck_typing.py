"""
#9. (Duck Typing - Another Practice)

Create a class named Car.
Requirements
Create a method named start().
It should print:
"Car Started"

Create another class named Bike.
Requirements
Create a method named start().
It should print:
"Bike Started"

Create another class named Truck.
Requirements
Create a method named start().
It should print:
"Truck Started"

Create a function named start_vehicle(vehicle).
Inside the function, call the start() method.
Create one object of each class.
Pass all three objects to the start_vehicle() function.
"""

class Car():
    
    def start(self):
        print("Car started")
        
class Bike():
    
    def start(self):
        print("Bike started")

class Truck():
    
    def start(self):
        print("Truck started")

car1 = Car()
bike1 = Bike()
truck1 = Truck()

def start_vehicle(vehicle):
    vehicle.start()
    
start_vehicle(car1)
start_vehicle(bike1)
start_vehicle(truck1)