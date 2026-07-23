"""
#4. Find Employees with Highest Salary
employees = [
    {"name": "Mayur", "salary": 50000},
    {"name": "Suraj", "salary": 75000},
    {"name": "Vishwas", "salary": 60000},
    {"name": "Varun", "salary": 90000}
]

Use max() with a lambda function to find the employee with the highest salary.

Expected:
{'name': 'Varun', 'salary': 90000}
"""

employees = [
    {"name": "Mayur", "salary": 50000},
    {"name": "Suraj", "salary": 75000},
    {"name": "Vishwas", "salary": 60000},
    {"name": "Varun", "salary": 90000}
]

highest_salary = max(employees, key=lambda x: x["salary"])
print(highest_salary)
'''
{'name': 'Varun', 'salary': 90000}
'''
