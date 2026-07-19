"""
#1. (Polymorphism - Method Overriding)

Create a class named Animal.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- name
Create a method named speak().
It should print:
"Animal makes a sound"

Create another class named Dog that inherits from Animal.
Override the speak() method.
It should print:
"Dog barks"

Create another class named Cat that inherits from Animal.
Override the speak() method.
It should print:
"Cat meows"

Create one Dog object and one Cat object.
Call the speak() method for both objects.
"""

class Animal():
    
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        print(f"Animal makes a sound")
        
class Dog(Animal):
    
    def speak(self):
        print(f"Dog barks")
        
class Cat(Animal):
    
    def speak(self):
        print(f"Cat meow")
        
dog1 = Dog("German Shepherd")
cat1 = Cat("Japnese Cat")

dog1.speak()
cat1.speak()

'''
Dog barks
Cat meow
'''

"""
## Why is this Polymorphism?

All objects have the same method name:
speak()
But they produce different behavior.
Dog.speak() → "Dog barks"
Cat.speak() → "Cat meow"

This is called Runtime Polymorphism (Method Overriding).
"""
