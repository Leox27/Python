"""
#12. (Hierarchical Inheritance)

Create a class named Person.
Requirements
Use the __init__() constructor.
The class should have these instance variables:
- name
- age
Create a method named display_person().
It should print:
- Name
- Age

Create a class named Student that inherits from Person.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- roll_no
Create a method named display_student().
It should print:
- Name
- Age
- Roll Number

Create another class named Teacher that inherits from Person.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- subject
Create a method named display_teacher().
It should print:
- Name
- Age
- Subject

Create one Student object and one Teacher object.
Call both display methods.
"""

class Person():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display_person(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        
class Student(Person):
    
    def  __init__(self, name, age, roll_no):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        
    def display_student(self):
        Person.display_person(self)
        print(f"Roll No.: {self.roll_no}")
        print()
        
class Teacher(Person):
    
    def __init__(self, name, age, subject):
        Person.__init__(self, name, age)
        self.subject = subject
        
    def display_teacher(self):
        Person.display_person(self)
        print(f"Subject: {self.subject}")
        
student = Student("Suraj Lohar", 21, 101)
teacher = Teacher("Birajdar Madam", 40, "Marathi")

student.display_student()
teacher.display_teacher()
'''
Name: Suraj Lohar
Age: 21
Roll No.: 101

Name: Birajdar Madam
Age: 40
Subject: Marathi
'''
