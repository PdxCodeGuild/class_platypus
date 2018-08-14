# Letter Grade
# By Skyler Parker
# Created on 14AUG18

# Imports

# Define global variables and lists

# Define Functions


def get_number():

    while True:
        try:
            expression = input('\nPlease enter an expression that you would like to have evaluated: ')
            answer = eval(expression)
            break
        except NameError:
            print('that\'s not a valid expression')
    print('\nYour answer is ' + str(answer))


# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Enter a new equation\n2 - Close Program'))

    if menu_answer == 1:
        get_number()

    else:
        break

