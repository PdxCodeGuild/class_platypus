# Letter Grade
# By Skyler Parker
# Created on 14AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Enter a new equation\n2 - Close Program'))

    if menu_answer == 1:
        expression_to_evaluate = input('Please enter an expression that you would like to have evaluated: ')
        answer = eval(expression_to_evaluate)
        print('Your answer is ' + str(answer))
    else:
        break

