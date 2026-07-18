"""
#5. (Class Methods)

Create a class named Employee.

Requirements
Use the __init__() constructor.
Create these instance variables:
- name
- employee_id
- salary

Create one class variable:
- company_name = "TCS"

Create a class method named change_company().
The method should take one parameter:
- new_company

The method should change the company_name to the new company.
Create a method named display() that prints:
- Employee Name
- Employee ID
- Salary
- Company Name

Create 2 employee objects.
Display their details.
Call the class method to change the company name to "Infosys".
Display both employees again and observe the change.
"""

class Employee():
    companay_name = "TCS"
    
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary
    
    @classmethod
    def change_company(cls, new_company):
        cls.companay_name = new_company
    
    def display(self):
        print(f"Employee name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        print(f"Company name: {Employee.companay_name}")
        # print(f"Company name: {type(self).companay_name}") both are same type(self) returns: <class '__main__.Employee'>
        print()

emp1 = Employee("Datta Gavali", 301, 12000)
emp2 = Employee("Kashinath Date", 302, 25000)

emp1.display()
emp2.display()
Employee.change_company("Infosys")
emp1.display()
emp2.display()
'''
Employee name: Datta Gavali
Employee ID: 301
Salary: 12000
Company name: TCS

Employee name: Kashinath Date
Employee ID: 302
Salary: 25000
Company name: TCS

Employee name: Datta Gavali
Employee ID: 301
Salary: 12000
Company name: Infosys

Employee name: Kashinath Date
Employee ID: 302
Salary: 25000
Company name: Infosys
'''
