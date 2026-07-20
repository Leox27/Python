"""
#1. (Public Members)

Create a class named Student.
Requirements
Use the __init__() constructor.
The class should have these public instance variables:
- name
- age
Create a method named display().
It should print:
- Name
- Age

Create one Student object.
Access and print the name directly using the object.
Change the name directly using the object.
Call display() again to verify the change.
"""

class Student():
    
    def __init__(self, name, age):
        self.name = name #public members
        self.age = age #public members
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
student1 = Student("Kumar Katekar", 23)

student1.display()
student1.name = "Mayur Jadhav"
student1.age = 21
student1.display()
'''
Name: Kumar Katekar
Age: 23
Name: Mayur Jadhav
Age: 21
'''
