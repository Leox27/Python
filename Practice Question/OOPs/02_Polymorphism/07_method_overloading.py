"""
#7. (Method Overloading in Python)

Create a class named Calculator.
Requirements
Create a method named add().
The method should work as follows:
- If 2 numbers are passed, print their sum.
- If 3 numbers are passed, print their sum.
- If 4 numbers are passed, print their sum.

Use Python's default arguments.
Create one Calculator object.

Call the add() method with:
- 2 numbers
- 3 numbers
- 4 numbers
"""

## Python's way of achieving method overloading.

# Using Default argument
class Calculator():
    
    def add(self, a, b, c=0, d=0): #default args
        print(a+b+c+d)
        
calc1 = Calculator()

calc1.add(10, 20)
calc1.add(10, 20, 30)
calc1.add(10, 20, 30, 40)
'''
30
60
100
'''

# Using (*args)
class Calculator:

    def add(self, *args):
        print(sum(args))

calc = Calculator()

calc.add(10, 20)
calc.add(10, 20, 30)
calc.add(10, 20, 30, 40)
calc.add(10, 20, 30, 40, 50)
'''
30
60
100
150
'''


"""
### This is not method overloading. It is called function aliasing (or creating aliases to function objects).
class Calculator():
    
    def add(self, a, b):
        return a+b
    prev1 = add

    def add(self, a, b, c):
        return a+b+c
    prev2 = add
    
    def add(self, a, b, c, d):
        return a+b+c+d

calc1 = Calculator()

print(calc1.prev1(10, 20))
print(calc1.prev2(10, 20, 30))
print(calc1.add(10, 20, 30, 40))"""