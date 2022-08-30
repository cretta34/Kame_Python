# challenge
class Account(object):

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        Account.count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
        else:
            print(f"残高は{self.balance}円です。残高が足りません。")

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()

    def show_balance(self):
        print("口座名{0.name}(口座番号{0.account_number})の残高は{0.balance}円です。".format(self))


myaccount = Account("my account", 1000)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(1500)
youraccount = Account("your account", 10000)
youraccount.deposit(5000)