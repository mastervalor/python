import re


class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= amount
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance: " , self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self  
    @classmethod
    def print_all_accounts(cls):
        for acc in cls.accounts:
            acc.display_account_info()
            
            
bank1 = BankAccount(1.3, 1000)
bank2 = BankAccount(1.8, 2000)

bank1.deposit(30).deposit(30).deposit(30).withdraw(60).yield_interest().display_account_info()
bank2.deposit(30).deposit(30).withdraw(60).withdraw(60).withdraw(60).withdraw(60).yield_interest().display_account_info()

BankAccount.print_all_accounts()