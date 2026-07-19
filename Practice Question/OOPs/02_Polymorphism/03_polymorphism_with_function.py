"""
#3. (Polymorphism with Function)

Create a class named Dog.
Requirements
Create a method named speak().
It should print:
"Dog barks"

Create another class named Cat.
Requirements
Create a method named speak().
It should print:
"Cat meows"

Create a function named animal_sound(animal).
Inside the function, call the speak() method.
Create one Dog object and one Cat object.
Call the animal_sound() function for both objects.
"""

class Dog():
    
    def speak(self):
        print(f"Dog barks")
        
class Cat():
    
    def speak(self):
        print(f"Cat meows")
    
dog1 = Dog()
cat1 = Cat()

def animal_sound(animal):
    animal.speak()
    
animal_sound(dog1)
animal_sound(cat1)
'''
Dog barks
Cat meows
'''


"""
## Why is this polymorphism?

The function:
animal_sound(animal)
doesn't know whether animal is a Dog or a Cat.

It simply calls:
animal.speak()
Python decides at runtime which speak() method to execute based on the object passed. That's runtime polymorphism.
"""
