class ATM:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def check_balance(self):
        dx = self.x
        return dx

    def calc_interest(self):
        v = self.x * .001
        y = v + self.x
        return y

    def deposit(self, w):
        self.x += w
        return w

    def withdraw(self, y):
        if self.x < y:
            print(f'You will overdraft you only have {self.x}')
            return
        else:
            self.x -= y
            return y

atm = ATM()



while True:
    user = input(f' What would you like to do? (deposit, withdraw, check balance,calculate interest, exit)')
    if user == 'exit':
        print('Goodbye')
        break
    if user == 'calculate interest':
        print(f' You have {atm.check_balance()} and have {atm.calc_interest()} after interest')
    if user == 'deposit':
        d_user = int(input(f'How much?'))
        atm.deposit(d_user)
        print(f' You now have {atm.check_balance()}')
    if user == 'withdraw':
        w_user = int(input(f'How much?'))
        if w_user > atm.check_balance():
            print(atm.withdraw(w_user))
        else:
            atm.withdraw(w_user)
            print(f'You have {atm.check_balance()} left.')
    if user == 'check balance':
        print(atm.check_balance())

# atm.deposit(20)
# # atm.withdraw()
# print(atm.check_balance())
# print(atm.calc_interest())