#lab 12 guess the number Version 1

import random

computer_guess = random.randint(1, 10)
game = 0

while game < 10:

    user_guess = int(input("Guess a number between 1 and 10:    "))

    if user_guess != computer_guess:
        print("Sorry, that was not the correct number. Try again!")

    else:
        print(f"You got it! {user_guess} was the right number.")
        break
    game += 1
