import math

class ATM:
    '''''' """Keeping track of bank balance, deposits, withdrawals, and interest. """
    def __init__(self, x=0, y=0.001):
        self.x = x
        self.y = y

    def balance(self):
        bx = self.x
        return bx

    def interest(self):
        i = self.x * 0.001
        y = i + self.x
        return y

    def deposit(self, d):
        self.x += d
        return d

    def withdraw(self, y):
        self.x -= y
        return y

    def print_history(self):
        return history

ATM = ATM()

history = []


# class ATM:
#     def __init__(self, balance, interest):  # this is the initializer
#         self.balance = balance  # these are member variables
#         self.interest = interest
#
#
# a = ATM(0, 0.001)  # call the initializer, instantiate the class
# print(a.balance)  # 0
# print(a.interest)

while True:
    ans = input(f'What would you like to do? Deposit, Withdrawal, Check Balance, History... ')
    if ans == "deposit":
        ans = int(input('How much would you like to deposit? '))



    # if ans == withdrawal:
    #     ans == int(input('How much would you like to withdrawal? '))
    #     print(ATM.withdraw())
    # if ans == balance:
    #     ans == int(input(f'Here is your balance{balance} '))
    # if ans == history:
    #     print(ATM.print_history())




