"""
#4. (Getter Method)

Create a class named BankAccount.
Requirements
Use the __init__() constructor.
Create these private instance variables:
- __account_holder
- __balance
Create a getter method named get_balance().
The method should return the private balance.

Create one BankAccount object.
Use the get_balance() method to access and print the balance.
Do not access __balance directly from outside the class.
"""

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
bank_acc1 = BankAccount("KD Comapany", 2500000)

print(bank_acc1.get_balance())
'''
2500000
'''


"""
Getter Method

- A getter method is used to access/read a private member.
- It is usually named with the prefix `get_`.
- It returns the value of the private member.
- The private member is not accessed directly from outside the class.

Example:
    def get_balance(self):
        return self.__balance
"""
