# Version 4 (optional)

import random

computer_guess = random.randint(1, 10)
user_guess_list = []

while True:

    user_guess = int(input("Guess a number between 1 and 10:    "))


    if user_guess != computer_guess:
        print("not quite. Try again.")
        user_guess_list.append(user_guess)

        if len(user_guess_list) > 1:
            if abs(computer_guess - user_guess_list[-1]) < abs(computer_guess - user_guess_list[-2]):
                print("You're closer")
            else:
                print("You're further away")
    else:
        print("You win")
        break
