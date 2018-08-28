class ATM:
    def __init__(self,balance=100,interestrate=0.01):
        self.balance = balance
        self.interestrate = interestrate

    def check_balance(self):
        check_balance = self.balance
        return check_balance

    def calculate_interest(self):
        balance = (self.balance * self.interestrate/100)+ self.balance
        return balance

    def deposit(self, deposit):
        self.balance += deposit
        return deposit

    def withdraw(self, amount):
        if self.balance < amount:
            return (f'overdraft you only have {self.balance}')
        else:
            self.balance -= amount
            return amount
    def print_transactions(self):
        return transact_history

atm = ATM()

transact_history = []

choice = input(f' Choose:(deposit, withdraw, check balance,calculate interest, history, exit)\n')
choice = choice.lower()
if choice == 'history':
        print(atm.print_transactions())
elif choice == 'calculate interest':
        print(f"You have {atm.check_balance()} and have {atm.calculate_interest()} including interest")
elif choice == 'deposit':
        deposit = int(input("How much you want to deposit?"))
        atm.deposit(deposit)
        transact_history.append(f'you deposited {deposit}')
        print(f"Your balnce is {atm.check_balance()}")

elif choice == 'withdraw':
        amount = int(input("How much money you want to withdraw?"))
        if amount > atm.check_balance():
            print(atm.withdraw(amount))
        else:
            atm.withdraw(w_user)
            transact_history.append(f'you withdrew {w_user}')
            print(f'You have {atm.check_balance()} left.')
elif choice == 'check balance':
        print(atm.check_balance())
elif choice == 'exit':
        print('Goodbye')
