"""
#6. (Getter and Setter with Validation)

Create a class named BankAccount.
Requirements
Use the __init__() constructor.
Create a private instance variable:
- __balance
Create these methods:
- get_balance()
- set_balance()

The get_balance() method should return the balance.
The set_balance() method should update the balance only if the new balance is greater than or equal to 0.

If the new balance is negative, print:
"Balance cannot be negative"

Create one BankAccount object.
Display the initial balance.
Try to set a valid balance.
Try to set a negative balance.
Display the final balance.
"""

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
    
    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

bank_acc1 = BankAccount("Mayur Jadhav", 100000000)
print(bank_acc1.get_balance())

bank_acc1.set_balance(110000000)
print(bank_acc1.get_balance())

bank_acc1.set_balance(-11000)
print(bank_acc1.get_balance())
'''
100000000
110000000
Balance cannot be negative
110000000
'''
    
"""
Getter and Setter with Validation

- A getter method is used to access/read a private member.
- A setter method is used to modify/update a private member.
- Validation can be added inside the setter before updating the value.
- This prevents invalid data from being assigned.

Example:

    def get_balance(self):
        return self.__balance

    def set_balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")
"""