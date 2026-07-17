### Question on Inheritance (One of the pillar of OOPs)

"""
Question 1 (Classes, Objects & Constructor)

Create a class named Student1.

Requirements
Use the __init__() constructor.
The class should have these instance variables:
name
roll_no
marks
Create a method named display() that prints all the student's details.
Create 3 student objects with different values.
Call the display() method for each object.
"""

class Student1():
    
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    
    def display_data(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.rollno}")
        print(f"Marks: {self.marks}")
        
student1 = Student1("Rahul", 101, 85)
student2 = Student1("Priya", 101, 91)
student3 = Student1("Aman", 101, 76)

student1.display_data()
student2.display_data()
student3.display_data()
'''
Name: Rahul
Roll No.: 101
Marks: 85
Name: Priya
Roll No.: 101
Marks: 91
Name: Aman
Roll No.: 101
Marks: 76
'''


"""
Question 2 (Instance Methods)

Create a class named Student2.

Requirements
Use the __init__() constructor.
The class should have these instance variables:
- name
- roll_no
- marks

Create a method named display() that prints all the student's details.
Create another method named is_pass().
If marks are 40 or more, print:
"<name> has Passed"
Otherwise, print:
"<name> has Failed"
Create 3 student objects.
At least one student should have marks less than 40.
Call both methods for every object.
"""

class Student2():
    
    def __init__(self, name, rollno, marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Roll No.: {self.rollno}")
        print(f"Marks: {self.marks}")
        print()
    
    def is_pass(self):
        print("*** Exam status ***")
        if self.marks >= 40:
            print(f"{self.name} is Passed")
        else:
            print(f"{self.name} is Failed")
        print()

student4 = Student2("Suraj", 101, 70)
student5 = Student2("kashinath", 101, 35)
student6 = Student2("Boomer", 101, 50)

student4.display()
student4.is_pass()
student5.display()
student5.is_pass()
student6.display()
student6.is_pass()

'''
Name: Suraj
Roll No.: 101
Marks: 70

*** Exam status ***
Suraj is Passed

Name: kashinath
Roll No.: 101
Marks: 35

*** Exam status ***
kashinath is Failed

Name: Boomer
Roll No.: 101
Marks: 50

*** Exam status ***
Boomer is Passed
'''


