"""
#2. (Abstract Class with Multiple Child Classes)

Create an abstract class named Vehicle.
Requirements
Import ABC and abstractmethod from the abc module.
Create an abstract method named start().
Create two child classes:
- Car
- Bike

Both classes must implement the start() method.
Car should print:
"Car starts with a key"
Bike should print:
"Bike starts with a self-start"

Create one object of Car and one object of Bike.
Call the start() method for both objects.
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass
    
class Car(Vehicle):
    
    def start(self):
        print("Car starts with a key")

class Bike(Vehicle):
    
    def start(self):
        print("Bike starts with a self-start")
        
car1 = Car()
bike1 = Bike()

car1.start()
bike1.start()
'''
Car starts with a key
Bike starts with a self-start
'''

