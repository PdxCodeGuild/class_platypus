# Rock Paper Scissor
# By Skyler Parker
# Created on 14AUG18

# Declare Variable
app_exit = False

player_score = 0

computer_score = 0

# Import
import random

# Define Variables and lists
computer_answer_list = [1, 2, 3]


# define Functions
def decide(answer):
    global computer_score
    global player_score
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
            computer_score += 1
        else:
            print('You won!')
            player_score += 1

    print('\nCurrent Score:\nPlayer --- ' + str(player_score) + '\nComputer --- ' + str(computer_score))


while app_exit != bool(True):
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


