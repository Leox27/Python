"""
#10. (Multilevel Inheritance)

Create a class named Person.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- name
Create a method named display_person().
It should print:
- Name

Create another class named Student that inherits from Person.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- roll_no
Create a method named display_student().
It should print:
- Name
- Roll Number

Create another class named CollegeStudent that inherits from Student.
Requirements
Use the __init__() constructor.
Create one new instance variable:
- college_name
Create a method named display_college_student().
It should print:
- Name
- Roll Number
- College Name

Create one CollegeStudent object.
Call display_college_student().
"""

class Person():
    
    def __init__(self, name):
        self.name = name
    
    def display_person(self):
        print(f"Name: {self.name}")
        
class Student(Person):
    
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no
        
    def display_student(self):
        super().display_person()
        print(f"Roll No.: {self.roll_no}")
        
class CollegeStudent(Student):
    
    def __init__(self, name, roll_no, college_name):
        super().__init__(name, roll_no)
        self.college_name = college_name
        
    def display_college_student(self):
        super().display_student()
        print(f"College name: {self.college_name}")
        
college_student1 = CollegeStudent("Sudarshan Kale", 105, "Z. P. Primary school")

college_student1.display_college_student()
'''
Name: Sudarshan Kale
Roll No.: 105
College name: Z. P. Primary school
'''
