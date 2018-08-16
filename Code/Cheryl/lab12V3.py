#version 3 Tell the user whether their guess is above ('too high!') or below ('too low!') the target value.

import random

computer_guess = random.randint(1, 10)
user_num_guesses = 0

while True:

    user_guess = int(input("Guess a number between 1 and 10:    "))

    if user_guess != computer_guess:
        user_num_guesses += 1
        if user_guess < computer_guess:
            print("You're too low. Try again!")
        else:
            print("You're too high. Try again!")

    else:
        print(f"You got it! {user_guess} was the right number. It took you {user_num_guesses} guesses!")
        break

