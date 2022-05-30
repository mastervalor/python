class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
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
        return self.balance
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self  
    @classmethod
    def print_all_accounts(cls):
        for acc in cls.accounts:
            acc.display_account_info()
            
class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = {
            "checking" : BankAccount(.02, 1000),
            "Savings" : BankAccount(.02, 2000)
        }
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(f"Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"Savings Balance: {self.account['Savings'].display_account_info()}")
        return self
    def transfer_money(self, amount, other_user,type):
        self.account[type].balance -= amount
        other_user.account[type].balance += amount
        self.display_user_balance()
        other_user.display_user_balance()
    def make_deposit(self, amount, type):
        self.account[type].deposit(amount)
        return self
    def make_withdrawal(self, amount, type):
        self.account[type].withdraw(amount)
        return self
    def display_user_balance(self):
        print(f"User: {self.first_name}, Checking Balance: {self.account['checking'].display_account_info()}")
        print(f"User: {self.first_name}, Savings Balance: {self.account['Savings'].display_account_info()}")
        return self
    
    
    
bob = User('bob', 'smith', 'bobs@', 45)
larry = User('larry', 'smith', 'lsmith@', 45)

bob.transfer_money(500,larry,'Savings')
bob.make_withdrawal(623, 'Savings')
bob.display_info()