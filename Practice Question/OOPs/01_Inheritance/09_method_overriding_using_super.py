"""
#9. (Using super() in Method Overriding)

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
Inside the overridden method:
- First call the parent class sound() method.
- Then print:
"Dog barks"

Create one Dog object.
Call the sound() method.
"""

class Animal():
    
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    
    def sound(self):
        super().sound()
        print("Dog Barks")

dog1 = Dog("Pit Bull")

dog1.sound()
'''
Animal makes a sound
Dog Barks
'''
