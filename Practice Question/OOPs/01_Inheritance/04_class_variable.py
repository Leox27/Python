"""
#4. (Class Variables)

Create a class named Employee.

Requirements

Use the __init__() constructor.

Create these instance variables:
- name
- employee_id
- salary

Create one class variable:
- company_name = "TCS"

Create a method named display() that prints:
- Employee Name
- Employee ID
- Salary
- Company Name

Create 3 employee objects.

Call the display() method for each object.

Finally, change the company name to "Infosys" using the class name.

Call display() again for all employees and observe the output.
"""

class Employee():
    companay_name = "TCS"
    
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary
    
    def display(self):
        print(f"Employee name: {self.emp_name}")
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
        print(f"Company name: {Employee.companay_name}")
        print()
        
emp1 = Employee("Datta Gavali", 301, 12000)
emp2 = Employee("Kashinath Date", 302, 25000)

emp1.display()
emp2.display()
Employee.companay_name = "Infosys"
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
