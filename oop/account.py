import time


class Account(object):

    count = 0

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.account_number = Account.count
        self.show_balance()
        self.transaction_history = []
        Account.count += 1

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.show_balance()
            self._add_transaction(-amount)
        else:
            print(f"残高は{self.balance}円です。残高が足りません。")

    def deposit(self, amount):
        self.balance += amount
        self.show_balance()
        self._add_transaction(amount)

    def show_balance(self):
        print("口座名{0.name}(口座番号{0.account_number})の残高は{0.balance}円です。".format(self))

    def _add_transaction(self, amount):
        transaction = {
            'withdraw/deposit': amount,
            'new_balance': self.balance,
            'time': Account._get_time_str()
        }
        self.transaction_history.append(transaction)

    @staticmethod
    def _get_time_str():
        current_time = time.localtime()
        return "{0.tm_year}年{0.tm_mon}月{0.tm_mday}日{0.tm_hour}時{0.tm_min}分".format(current_time)

    def show_transaction_history(self):
        for transaction in self.transaction_history:
            transaction_str_list = []
            for k, v in transaction.items():
                transaction_str_list.append(f"{k}: {v}")
            print(", ".join(transaction_str_list))


myaccount = Account("my account", 1000)
print(myaccount.balance)
myaccount.withdraw(300)
myaccount.deposit(500)
myaccount.withdraw(1500)
youraccount = Account("your account", 10000)
youraccount.deposit(5000)
print(myaccount.transaction_history)
myaccount.show_transaction_history()