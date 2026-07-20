"""
Question 25 (Protected Members)

Create a class named Employee.
Requirements
Use the __init__() constructor.
The class should have these protected instance variables:
- _name
- _salary
Create a method named display().
It should print:
- Name
- Salary

Create one Employee object.
Call the display() method.
Access the protected members directly using the object and print them.
"""

class Employee():
    
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self._salary}")
        
emp1 = Employee("Kashinath Date", 700000)

# emp1.display()

# access directly protected member
print(emp1.name)
print(emp1._salary)

# modify directly protected member
emp1._salary = 1000000
emp1.display()
'''
Kashinath Date
700000
Name: Kashinath Date
Salary: 1000000
'''


"""
Protected Members

- Protected members are created using a single underscore (_).
- They are intended to be used inside the class and its child classes.
- In Python, protected members are only a convention (not strictly enforced).
- They can still be accessed and modified from outside the class.
- Example:
    self._name
    self._salary
"""
