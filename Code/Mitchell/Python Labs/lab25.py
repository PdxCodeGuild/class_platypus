class ATM:
    # Initializes ATM account no history & balance of 0
    def __init__(self, balance = 0.00, history = []):
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

# Declares ATM class and action that user will enter
atm = ATM()
action = ''
# Continuously asks user for action until they quit
while action != 'quit':
    action = input('What would you like to do? (Type "deposit", "withdraw", "check balance", "history" or "quit") ').lower()
    # Deposit the amount given into users ATM account
    if action == 'deposit':
        amount = input('How much would you like to deposit? ')
        atm.deposit(float(amount))
    # Withdraws passed amount from balance if possible
    elif action == 'withdraw':
        amount = input('How much would you like to withdraw? ')
        atm.withdraw(float(amount))
    # Returns the current balance of the account
    elif action == 'check balance':
        print(f'Current balance is ${round(atm.check_balance(), 2)}.')
    # Prints out a user's transaction history
    elif action == 'history':
        atm.print_transactions()
    # If user types quit, exit program
    elif action == 'quit':
        break
    # Else the user typed an invalid option
    else:
        print('ERROR: You did not type a valid option, pleas type ether "deposit", "withdraw", "check balance", "history" or "quit".')