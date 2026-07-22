"""
#5. (Abstract Class with Constructor and Multiple Methods)

Create an abstract class named Employee.
Requirements
Use the __init__() constructor to store:
- name
- salary

Create a normal method named display_details().
It should print the employee name and salary.
Create two abstract methods:
- calculate_bonus()
- work()

Create a child class named Developer.

Implement both abstract methods.
calculate_bonus():
    Return 10% of the salary.
work():
    Print:
    "Developer writes code"

Create a Developer object.
Display the employee details.
Call work().
Calculate and print the bonus.
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def display_details(self):
        print(f"Employee name: {self.name}")
        print(f"Salary: {self.salary}")
    
    @abstractmethod
    def calculate_bonus(self):
        pass
    
    @abstractmethod
    def work(self):
        pass
    
class Developer(Employee):
    
    def calculate_bonus(self):
        return f"{self.name}'s bonus is {self.salary*0.1}"
    
    def work(self):
        print(f"Developer writes code")
        
dev1 = Developer("Mayur Jadhav", 700000)

dev1.display_details()
dev1.work()
print(dev1.calculate_bonus())
'''
Employee name: Mayur Jadhav
Salary: 700000
Developer writes code
Mayur Jadhav's bonus is 70000.0
'''
