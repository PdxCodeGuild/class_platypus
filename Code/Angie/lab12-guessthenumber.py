import random

x = random.randint(1, 10)
print(x)
c = 0


while True:

    user = int(input('Guess the number between 1 and 10\n'))

    if x == user:
        print('Winner Winner Chicken Dinner')
        break
    else:
        print('Sorry try again')

    perform = input('Do you want to guess again?').lower()
    if perform == 'no':
        break