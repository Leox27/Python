"""
#6. (Property Decorator)

Create a class named BankAccount.
Requirements
Use the __init__() constructor.
Create a private instance variable:
- __balance

Use the @property decorator to create a getter for balance.
Use the @balance.setter decorator to create a setter for balance.

The balance should be updated only if the new balance is greater than or equal to 0.
If the new balance is negative, print:
"Balance cannot be negative"

Create one BankAccount object.
Read the balance using:
bank_acc1.balance
Update the balance using:
bank_acc1.balance = new_balance
Display the updated balance.
"""

class BankAccount():
    
    def __init__(self, account_holder, balance):
        self.__account_holder = account_holder
        self.__balance = balance
        
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

bank_acc1 = BankAccount("Vishwas Vedpathak", 25000)

print(bank_acc1.balance)

bank_acc1.balance = 10000
print(bank_acc1.balance)
'''
25000
10000
'''


"""
@property Decorator

- The @property decorator is used to access a private member like a normal attribute.
- It works as a getter.
- The @property method does not need parentheses when accessed.

Example:
    @property
    def balance(self):
        return self.__balance

Access:
    print(bank_acc1.balance)

- The @property_name.setter decorator is used to modify the private member.
- Validation can be added inside the setter.

Example:
    @balance.setter
    def balance(self, new_balance):
        if new_balance >= 0:
            self.__balance = new_balance
        else:
            print("Balance cannot be negative")

Modify:
    bank_acc1.balance = 10000

- @property provides controlled access to private members.
- It is the modern Pythonic way of implementing getters and setters.
"""
