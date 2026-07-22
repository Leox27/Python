"""
#3. (Abstract Class with Constructor and Normal Method)

Create an abstract class named Employee.
Requirements
Use the __init__() constructor to store:
- name
Create a normal method named display_name().
It should print the employee name.
Create an abstract method named work().

Create two child classes:
- Developer
- Tester

Both classes must implement the work() method.
Developer should print:
"Developer writes code"
Tester should print:
"Tester tests the software"

Create one Developer object and one Tester object.
Call both:
- display_name()
- work()
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    
    def __init__(self, name):
        self.name = name
    
    def display_name(self):
        print(f"Name: {self.name}")
        
    @abstractmethod
    def work(self):
        pass
    
class Developer(Employee):
    
    def work(self):
        print("Developer writes code")
        
class Tester(Employee):
    
    def work(self):
        print("Tester tests the software")
        
dev1 = Developer("Datta Gavali")
test1 = Tester("Kashinath Date")

dev1.display_name()
dev1.work()
test1.display_name()
test1.work()
'''
Name: Datta Gavali
Developer writes code
Name: Kashinath Date
Tester tests the software
'''
