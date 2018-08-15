# Guess the Number
# By Skyler Parker
# Created on 14AUG18

# Imports

import random

# Define global variables and lists

# Define Functions


def random_number_generator():
    x = random.randint(1,10)
    return x


# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - You Guess\n2 - Computer Guesses\n3 - Close Program'))

    if menu_answer == 1:
        user_guess = 0
        computer_answer = random_number_generator()
        number_of_guesses = 0
        old_difference = 0
        new_difference = 0

        while user_guess != computer_answer:
            user_guess = int(input('Guess a number between 1 and 10'))

            number_of_guesses += 1
            new_difference = abs(user_guess-computer_answer)
            if number_of_guesses > 1:
                if new_difference < old_difference:
                    print('You are getting warmer, but still not there!')
                elif new_difference > old_difference:
                    print('You are getting colder >.<')
                else:
                    print('why are you guessing the same number?')
            old_difference = new_difference
        print('Congratulations! You guessed it after ' + str(number_of_guesses) + ' tries!')

    elif menu_answer == 2:
        number_of_guesses = 0
        computer_answer = 0

        user_answer = int(input('Please select a number between 1 and 10'))

        while computer_answer != user_answer:
            computer_answer = random_number_generator()
            number_of_guesses += 1

        print('The computer guessed your number after ' + str(number_of_guesses) + ' tries!')


    else:
        break