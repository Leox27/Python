# class Bank:
#     b_name = "Karnataka Bank"
#     b_loc = "Pune"
#     b_total_Account = 0

#     def __init__(self, c_name, c_bal):
#         self.c_name = c_name
#         self.c_bal = c_bal

#     @classmethod
#     def Display_Bank(cls):
#         print(cls.b_name, cls.b_loc, cls.b_total_Account)
#     @classmethod
#     def Update_Account(cls):
#         cls.b_total_Account+=1
#     @classmethod
#     def Update_loc(cld, new_loc):
#         cld.b_loc=new_loc
# c1=Bank("Suresh", 5000)
# Bank.Display_Bank()
# c1.Update_loc("Mumbai")
# c1.Display_Bank()


##
class ATM_SBI:
    Bank_name = "SBI"
    location = "Pune"

    def __init__(self, name, bal):
        self.name = name
        self.bal = 2000
    
    def Display(self):
        print(self.Bank_name, self.location, self.name, self.bal)

    def check_bal(self):
        print(f"available balance: Rs. {self.bal}")

    def deposite(self):
        new_deposite = int(input("Enter the amount: "))
        self.bal += new_deposite

    def withdraw(self):
        new_withdraw = int(input("Enter the amount: "))
        if self.bal < new_withdraw:
            print("Your acccount balance is low !!!")
        else:
            self.bal -= new_withdraw

c1 = ATM_SBI("raj", 1234)
c1.check_bal()
c1.deposite()
c1.Display()
c1.withdraw()
c1.Display()
