"""
#5. (Setter Method)

Create a class named BankAccount.
Requirements
Use the __init__() constructor.
Create a private instance variable:
- __balance

Create a setter method named set_balance().
The method should accept a new balance and update __balance.

Create one BankAccount object.
Use the set_balance() method to change the balance.
Use the get_balance() method to verify the updated balance.
Do not modify __balance directly from outside the class.
"""

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        self.__balance = new_balance

bank_acc1 = BankAccount("Mayur Jadhav", 100000000)
print(bank_acc1.get_balance())

bank_acc1.set_balance(110000000)
print(bank_acc1.get_balance())
'''
100000000
110000000
'''


"""
Setter Method

- A setter method is used to modify/update a private member.
- It is usually named with the prefix `set_`.
- It accepts a new value as an argument.
- It updates the private member inside the class.
- A setter usually does not return anything.

Example:
    def set_balance(self, new_balance):
        self.__balance = new_balance

Usage:
    bank_acc.set_balance(50000)
"""    

    