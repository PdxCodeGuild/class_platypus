import random


print('Welcome to Rock, Paper, Scissors, Lizard, Spock!')
choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
user_choice = input('Please choose rock, paper, scissors, lizard, or spock. >  ').lower()
computer_choice = random.choice(choices)

#indexes 0-1 lose, indexes 2-3 win
rock_dict = {'rock': ['paper', 'spock', 'scissors', 'lizard']}
paper_dict = {'paper': ['scissors', 'lizard', 'spock', 'rock']}
scissors_dict = {'scissors': ['rock', 'spock', 'paper', 'lizard']}
lizard_dict = {'lizard': ['rock', 'scissors', 'spock', 'paper']}
spock_dict = {'spock': ['lizard', 'paper', 'rock', 'scissors']}

