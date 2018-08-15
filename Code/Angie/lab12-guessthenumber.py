import random

x = random.randint(1, 10)
print(x)
counter = 0


while True:

    user = int(input('Guess the number between 1 and 10\n'))
    counter += 1
    if x == user:
        print(f'Winner Winner Chicken Dinner {counter}')
        break
    else:
        print(f'Sorry try again {counter}')

    perform = input('Do you want to guess again?').lower()
    if perform == 'no':
        break