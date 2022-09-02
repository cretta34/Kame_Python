# 直接balanceにアクセスして更新できてしまう
# _balanceとするとnonpublicにできるがそれでも強制力はない
class Account:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()

    def withdraw(self, amount):
        if self.__balance < amount:
            print("残高が足りません")
        else:
            self.__balance -= amount
            self.show_balance()

    def show_balance(self):
        print(f"残高は{self.__balance}円です")


myaccount = Account(10000)
print(dir(myaccount))
myaccount.deposit(2000)
myaccount.withdraw(5000)
myaccount.withdraw(10000)
myaccount.__balance = -10000
print(myaccount.__balance)
myaccount.show_balance()
print(dir(myaccount))
# 名前修飾でも直接変更することはできる.普通はしない
myaccount._Account__balance = -100000
myaccount.show_balance()