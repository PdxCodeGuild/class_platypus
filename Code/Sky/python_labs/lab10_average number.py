# Average Number
# By Skyler Parker
# Created on 16AUG18

# Imports
import random
# Define global variables and lists

# Define Functions

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Find an average number\n2 - Close Program'))

    if menu_answer == 1:
        numbers = []
        while True:
            num = input('Enter a number, or "done": ')
            if num == 'done':
                break
            else:
                numbers.append(num)
        if len(numbers) == 0:
            print('\n\nYou entered no numbers, would you like to try again?')
        else:
            print('\n')
            print(numbers)

    else:
        break

