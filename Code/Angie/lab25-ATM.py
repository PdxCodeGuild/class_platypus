# default balance 0, interest rate 0.001%


class ATM:
    def __init__(self, balance, interest):
        self.balance = balance
        self.interest = interest

    def check_balance(balance):
        pass

    def deposit(amount):
        pass

    def check_withdrawal(amount):
        pass

    def withdraw(amount):
        pass

    def calc_interest(interest):
        interest = (balance * .001) + balance

    return calc_interest()


atm = ATM(0, .001)
print(atm.check_balance())  # "your balance is $0"
atm.deposit(5)
print(atm.check_balance())  # "your balance is $5"
print(atm.check_withdrawal(10))  # False
print(atm.withdraw(2))  # 2
print(atm.check_balance())  # "your balance is $3"



