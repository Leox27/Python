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