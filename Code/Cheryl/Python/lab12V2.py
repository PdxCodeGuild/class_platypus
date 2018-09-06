# Version 2


import random

computer_guess = random.randint(1, 10)
user_num_guesses = 0

while True:

    user_guess = int(input("Guess a number between 1 and 10:    "))

    if user_guess != computer_guess:
        print("Sorry, that was not the correct number. Try again!")
        user_num_guesses += 1

    else:
        print(f"You got it! {user_guess} was the right number. It took you {user_num_guesses} guesses!")
        break
