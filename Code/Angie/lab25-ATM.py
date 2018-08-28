# default balance 0, interest rate 0.001%


class ATM:
    def __init__(self, balance=0, interest=0.001):
        self.balance = balance
        self.interest = interest

    def check_balance(self):  # returns account balance
        return f'Your balance is currently at ${self.balance}'

    # def print_transactions(self):  # maintains a list of transactions
    #     transact = []
    #     for deposit in :
    #         transact.append(deposit)
    #
    #

    def deposit(self, amount):  # deposits the given amount into account
        self.balance += amount

    def check_withdrawal(self, amount):  # returns true if the withdrawn amount wont put the account in the negative
        self.balance -= amount <= 0
        return False

    def withdraw(self, amount):  # withdraws the amount from the account and returns it
        pass

    # def calc_interest(self, interest):  # returns the amount of interest
    #     interest = (balance * .001) + balance




atm = ATM()
print(atm.check_balance())  # "your balance is $0"
atm.deposit(5)
print(atm.check_balance())  # "your balance is $5"
print(atm.check_withdrawal(10))  # False
# print(atm.withdraw(2))  # 2
# print(atm.check_balance())  # "your balance is $3"
#
#
# while True:
#     user = input('what would you like to do (deposit, withdraw, check balance, history)?')
# deposit
# how much would you like to deposit?
# $5
# what would you like to do (deposit, withdraw, check balance, history)?
# check balance
# balance: $5