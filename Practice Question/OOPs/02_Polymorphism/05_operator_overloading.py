"""
#5. (Operator Overloading)

Create a class named Number.
Requirements
Use the __init__() constructor.
The class should have one instance variable:
- value

Overload the + operator using the __add__() method.
The method should return the sum of two Number objects.

Create two Number objects.
Add them using the + operator.
Print the result.
"""

class Number():
    
    def __init__(self, value):
        self.value = value
        
    def __add__(self, other):
        return self.value + other.value
    
num1 = Number(10)
num2 = Number(20)
print(num1+num2)
'''
30
'''

