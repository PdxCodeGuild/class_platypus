import random


print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')



#create function
def game():
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    user_choice = input('Please choose rock, paper, scissors, lizard, or Spock. >  ').lower()
    computer_choice = random.choice(choices)

    #indexes 0-1 lose, indexes 2-3 win
    rps_dict = {'rock': ['paper', 'spock', 'scissors', 'lizard'], 'paper': ['scissors', 'lizard', 'spock', 'rock'], 'scissors': ['rock', 'spock', 'paper', 'lizard'], 'lizard': ['rock', 'scissors', 'spock', 'paper'], 'spock': ['lizard', 'paper', 'rock', 'scissors']}


    print(f'\tYou chose: {user_choice.upper()}.\n\tThe computer chose: {computer_choice.upper()}.')

    # if rps_dict[user_choice]:
    #     print(f'HELLLLOOOOOO + {user_choice}')

    if user_choice in rps_dict:
        if computer_choice in rps_dict[user_choice]:
            print(rps_dict[user_choice])




print(game())