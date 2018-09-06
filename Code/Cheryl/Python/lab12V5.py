#binary search
import random


computer_num_guesses = 0

while True:

    user_guess = int(input("What number would you like the computer to guess? >    "))
    computer_guess = random.randint(1, 10)
    if computer_guess != user_guess:
        computer_guess = random.randint(1, 10)
        computer_num_guesses += 1

    else:
        print(f"The computer guessed it! You chose the number {user_guess}. It took the computer {computer_num_guesses} guesses!")
        break