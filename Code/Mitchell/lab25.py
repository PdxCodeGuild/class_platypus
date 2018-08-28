class ATM:
    # Initializes ATM account no history & balance of 0
    def __init__(self, balance = 0, history = []):
        self.balance = balance
        self.history = history
    # Method that checks the current balance of ATM
    def check_balance(self):
        return self.balance
    # Deposits passed amount into ATM account
    def deposit(self, amount):
        self.balance += amount
        self.history.append('User deposited $' + str(amount))
    # Returns true if amount can be withdrawn from balance
    def check_withdrawal(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False
    # Withdraws passed amount from ATM balance
    def withdraw(self, amount):
        if self.check_withdrawal(amount):
            self.balance -= amount
            self.history.append('User withdrew $' + str(amount))
        else:
            print('ERROR: Withdraw amount is larger than current balance.')
    # Calculates amount of interest on ATM account
    def calc_interest(self):
        return self.balance + (self.balance * 0.001)
    # Prints list of all transactions performed
    def print_transactions(self):
        print('Transaction History')
        print('-------------------')
        for i in range(len(self.history)):
            print(self.history[i])
        print('-------------------')
# Print statements for debugging
atm = ATM()
print(atm.check_balance())  # "your balance is $0"
atm.deposit(5)
print(atm.check_balance())  # "your balance is $5"
print(atm.check_withdrawal(10))  # False
print(atm.withdraw(2))  # 2
print(atm.check_balance())  # "your balance is $3"
print(atm.print_transactions())