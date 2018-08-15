import random

x = random.randint(1, 10)
counter = 0


while True:

    user = int(input('Guess the number between 1 and 10, you get 10 tries.\n'))
    counter += 1
    if x == user:
        print(f'Winner Winner Chicken Dinner! You guessed {counter} times')
        break

    if counter == 10:
        print('you guessed 10 times! Sorry you lose.')
        break

    else:
        print(f'Sorry try again! You guessed {counter} times')

    perform = input('Do you want to guess again?').lower()
    if perform == 'no':
        break