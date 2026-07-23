"""
#2. (Lambda Function)

Create a lambda function named maximum.
It should accept two numbers
and return the greater number.
Call it with:
25 and 40
Print the result.
"""

maximum = lambda num1, num2: num1 if num1 > num2 else num2
print(maximum(25, 40))
'''
40
'''
