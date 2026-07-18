"""
#7. (Single Inheritance)

Create a class named Person.

Requirements
Use the __init__() constructor.

The class should have these instance variables:
- name
- age
Create a method named display_person() that prints:
- Name
- Age

Create another class named Student that inherits from Person.
Use the __init__() constructor.

The Student class should have one new instance variable:
- roll_no
Create a method named display_student() that prints:
- Name
- Age
- Roll Number

Create 2 Student objects.
Call display_student() for both objects.
"""

class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    
    def __init__(self, name, age, roll_no):
        super().__init__(name, age) #constructor chaining
        self.roll_no = roll_no
    
    def display_student(self):
        super().display_person() #method chaining
        print(f"Roll No.: {self.roll_no}")

Student1 = Student("Tejas Patil", 22, 101)
Student2 = Student("Varun Mane", 22, 102)

Student1.display_student()
Student1.display_student()

Student3 = Person("Vishwas Vedpathak", 22)
Student4 = Person("Mayur Jadhav", 21)

Student3.display_person()
Student4.display_person()
'''
Name: Tejas Patil
Age: 22
Roll No.: 101
Name: Tejas Patil
Age: 22
Roll No.: 101
Name: Vishwas Vedpathak
Age: 22
Name: Mayur Jadhav
Age: 21
'''
