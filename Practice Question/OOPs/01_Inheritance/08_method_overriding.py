"""
#8. (Method Overriding)

Create a class named Animal.

Requirements
Use the __init__() constructor.
The class should have one instance variable:
- name

Create a method named sound().
It should print:
"Animal makes a sound"

Create another class named Dog that inherits from Animal.
Override the sound() method.
It should print:
"Dog barks"
Create one Dog object.
Call the sound() method.
"""

class Animal():
    
    def __init__(self, name):
        self.name = name
        
    def sound(self):
        print("Animal makes sound")

class Dog(Animal):
    
    def sound(self):
        # super().sound()
        print("Dog Barks... Bhow bhow bhow")

dog1 = Dog("German Shepherd")
dog1.sound()
dog1 = Animal("German Shepherd")
dog1.sound()
'''
Dog Barks... Bhow bhow bhow
Animal makes sound
'''
