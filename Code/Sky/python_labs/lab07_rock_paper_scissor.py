# Rock Paper Scissor
# By Skyler Parker
# Created on 14AUG18


# Import
import random

# Define Variables and lists
app_exit = False
computer_answer_list = [1, 2, 3]

results = {'player': 0, 'computer': 0, 'tie': 0}


# define Functions
def decide(answer):
    computer_answer = random.choice(computer_answer_list)

    if computer_answer == 1:
        print('The computer chose Rock')
    elif computer_answer == 2:
        print('The computer chose Paper')
    else:
        print('The computer chose Scissor')

    if answer == computer_answer:
        print('You and the computer tied >.<')
    else:
        result = int(computer_answer - answer)
        if (result == 1) or (result == -2):
            print('The computer won, boo!')
            results['computer'] += 1
        else:
            print('You won!')
            results['player'] += 1

    print('\nCurrent Score:\nPlayer --- ' + str(results['player']) + '\nComputer --- ' + str(results['computer']))


while not app_exit:
    menu_answer = int(input('\nMenu:\n\n1 - Rock\n2 - Paper\n3 - Scissor\n4 - Close Program'))

    # Declare Variables
    print('-'*10 + 'RESULTS!' + '-'*10 + '\n')
    if menu_answer == 1:
        print("You chose Rock")
        decide(1)
    elif menu_answer == 2:
        print('You chose Paper')
        decide(2)
    elif menu_answer == 3:
        print('You chose Scissor')
        decide(3)
    else:
        app_exit = True

    print('\n' + '-' * 28 + '\n')

