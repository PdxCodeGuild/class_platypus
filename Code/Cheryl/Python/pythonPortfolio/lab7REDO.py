import random


print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')



#create function
def game():
    play = 'yes'
    while play == 'yes':
        choices = ['rock', 'paper', 'scissors', 'spock', 'lizard']
        computer_choice = random.choice(choices)
        user_choice = input('Please choose rock, paper, scissors, lizard, or Spock. >  ').lower()
        # true is lose// false is win
        rps_dict = {'rock': {'paper': True, 'scissors': False, 'lizard': False, 'spock': True}, 'paper': {'rock': False, 'scissors': True, 'lizard': True, 'spock': False}, 'scissors': {'paper': False, 'rock': True, 'lizard': False, 'spock': True}, 'lizard': {'rock': True, 'spock': False, 'scissors': True, 'paper': False}, 'spock': {'lizard': True, 'scissors': False, 'paper': True, 'rock': False}}

        print(f'\tYou chose: {user_choice.upper()}.\n\tThe computer chose: {computer_choice.upper()}.')

        if computer_choice == user_choice:
            print(f'\tBoth you and the computer chose {user_choice}, so it\'s a tie.')
        else:
            bad_name = rps_dict[user_choice][computer_choice]
            if bad_name == False:
                print(f'\t{user_choice.upper()} beats {computer_choice.upper()}. You WIN!')
            else:
                print(f'\t{computer_choice.upper()} beats {user_choice.upper()}. You Lose.')
        play = input('Would you like to play again? ').lower()


game()
print('Thanks for playing!')

