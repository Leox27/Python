"""
#3. (Private Members)

Create a class named BankAccount.
Requirements
Use the __init__() constructor.
The class should have these private instance variables:
- __account_holder
- __balance
Create a method named display().
It should print:
- Account Holder
- Balance

Create one BankAccount object.
Call the display() method.
Try to access __balance directly using the object.
Observe what happens.
"""

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def display(self):
        print(f"Account holder: {self.__account_holder}")
        print(f"Balance: {self.__balance}")
        
bank_acc1 = BankAccount("Balaji Date", 5000000)

# bank_acc1.display()

print(bank_acc1.__account_holder)
print(bank_acc1.__balance)

bank_acc1.__account_holder = "Mayur Jadhav"
bank_acc1.__balance = 0

print(bank_acc1.__account_holder)
print(bank_acc1.__balance)
'''
'''


"""
Private Members

- Private members are created using double underscores (__).
- They are intended to be used only inside the class.
- Python uses name mangling to make direct access difficult.
- They cannot be accessed directly using object.__variable.
- They should be accessed or modified using class methods (getter/setter).
- Example:
    self.__name
    self.__balance
"""
