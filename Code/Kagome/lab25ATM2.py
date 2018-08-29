import math

class ATM:
    '''''' """Keeping track of bank balance, deposits, withdrawals, and interest. """
    def __init__(self, x=0, y=0.001):      #can use (self, balance=0, interest=0.001) instead of x,y
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

    def withdrawal(self, y):
        self.x -= y
        return y

    def trans_history(self):
        return trans_history

ATM = ATM()

trans_history = []


while True:
    ans = input('What would you like to do? Deposit, Withdrawal, Check Balance, History or Exit... ').lower()
    if ans == "deposit":
        ans = int(input('How much would you like to deposit? '))



    # if ans == withdrawal:
    #     ans == int(input('How much would you like to withdrawal? '))
    #     print(ATM.withdraw())

    # elif ans == balance:
    #     ans == int(input(f'Here is your balance{balance} '))

    # elif ans == history:
    #     print(ATM.trans_history())

    #elif ans == Exit:
    #print('Goodbye.')




