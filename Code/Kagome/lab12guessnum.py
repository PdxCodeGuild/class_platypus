import random
num1 = random.randint(1, 10)

while True:
    guess_number = input('Guess a number between 1 and 10! ')
    guess_number = int(guess_number)

    if guess_number > num1:
        print('You guessed too high!')
    if guess_number < num1:
        print('You guessed too low.')

    elif guess_number == num1:
        print('You guessed correctly!')
        break










