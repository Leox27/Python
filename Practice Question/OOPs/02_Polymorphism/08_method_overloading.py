"""
#8. (Method Overloading using *args)

Create a class named Calculator.
Requirements
Create a method named multiply().
The method should accept any number of arguments using *args.
It should print the multiplication of all the numbers passed.

Create one Calculator object.
Call the multiply() method with:
- 2 numbers
- 3 numbers
- 5 numbers
"""

class Calculator():
    
    def multiply(self, *args):
        multiplication = 1
        for i in args:
            multiplication *= i
        print(multiplication)

calc1 = Calculator()

calc1.multiply(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        