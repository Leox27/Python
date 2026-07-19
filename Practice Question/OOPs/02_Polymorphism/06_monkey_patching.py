"""
#6. (Monkey Patching)

Create a class named Student.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- name
Create a method named display().
It should print:
"Student Name: <name>"

Create one Student object.
After creating the object, create a new method named greet() outside the class.
The greet() method should print:
"Hello <name>"

Attach the greet() method to the Student object using monkey patching.
Call both display() and greet().
"""

class Student():
    
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Name: {self.name}")
        
student1 = Student("Nikhil Shinde")

def greet(self):
    print(f"Hello, \n{self.name}")

# Monkey Patching (Class level)
Student.greet = greet                   #class_name.function_name = function_name

student1.display()
student1.greet()
'''
Name: Nikhil Shinde
Hello, 
Nikhil Shinde
'''


"""
class Student():
    
    def __init__(self, name):
        self.name = name
    def display(self):
        print(f"Name: {self.name}")
        
student1 = Student("Nikhil Shinde")

def greet(self):
    print(f"Hello, \n{self.name}")
    
# Monkey Patching
from types import MethodType
student1.greet = MethodType(greet, student1)

student1.display()
student1.greet()
"""
