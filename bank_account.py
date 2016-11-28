'''
Problem 1: Bank account
Create a file named bank_account.py. In it, write a class named BankAccount that represents a bank account. It should have two account balances, one for checking and one for savings, that can be deposited and withdrawn from.


BankAccount should have the following functions defined inside it:
deposit_into_savings(amount)
Adds the given amount to the savings account balance. You can assume amount is an int or float.
deposit_into_checking(amount)
Adds the given amount to the checking account balance. You can assume amount is an int or float.
withdraw(amount)
Subtracts the amount from the checking account balance. If the checking account balance reaches $0, the remaining amount should be subtracted from the savings account balance. For example, if the account balances are: checking = $10 and savings = $15, and $20 is withdrawn, the final account balances would be checking = $0 and savings = $5.


The initial checking and savings account balances are specified when the BankAccount object is created. This means that you need to define an __init__ function in your BankAccount class that takes in those two parameters.


Some additional requirements:
The checking and savings account balances should be printed at the end of every BankAccount function.
An account balance can be negative (though remember the requirement that if the checking account reaches $0 during a withdrawal, the savings account should be used for the remaining amount).
You should be able to create multiple BankAccount objects with different balances.


Below is an example of how an object of this class should work.


Example
>>> my_account = BankAccount(20, 50)
Checking account balance: $20
Savings account balance: $50
>>> my_account.deposit_into_checking(20)
Checking account balance: $40
Savings account balance: $50
>>> my_account.deposit_into_savings(10)
Checking account balance: $40
Savings account balance: $60
>>> my_account.withdraw(80)
Checking account balance: $0
Savings account balance: $20
>>> my_account.withdraw(50)
Checking account balance: $0
Savings account balance: $-30


'''

class BankAccount:
    def __init__(self, var1, var2):
      self.checking = var1
      self.savings = var2
      print("Checking account balance: $", self.checking)
      print("Savings account balance: $", self.savings)
    def deposit_into_savings(self, amount):
      self.savings += amount
      print("Checking account balance: $", self.checking)
      print("Savings account balance: $", self.savings)
    def deposit_into_checking(self, amount):
      self.checking += amount
      print("Checking account balance: $", self.checking)
      print("Savings account balance: $", self.savings)
    def withdraw(self, amount):
      self.checking -= amount
      if self.checking <= 0:
        #variable to hold the negative balance
        neg_balance = self.checking
        self.savings += neg_balance
        self.checking = 0  
      print("Checking account balance: $", self.checking)
      print("Savings account balance: $", self.savings)
        
      
        
my_account = BankAccount(20, 50)
my_account.deposit_into_checking(20)
my_account.deposit_into_savings(10)
my_account.withdraw(80)
my_account.withdraw(50)



