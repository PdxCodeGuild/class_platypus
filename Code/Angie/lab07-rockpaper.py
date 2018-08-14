import random

compy = random.choice(['rock', 'paper', 'scissors', 'spock'])

while True:
    user = input('which do you choose? rock, paper or scissors?')

    while user not in ['rock', 'paper', 'scissors']:
        user = input('Which do you choose rock, paper or scissors?>').lower()

    if user == 'rock' and compy == 'rock':
        print('rock vs. rock! it is a tie!')

    elif user == 'rock' and compy == 'paper':
        print('rock vs. paper! paper wins.')

    elif user == 'rock' and compy == 'scissors':
        print('rock vs. scissors! rock wins.')

    elif user == 'rock' and compy == 'spock':
        print('rock vs. spock! spock wins!')

    elif user == 'paper' and compy == 'paper':
        print('paper vs. paper! it is a tie.')

    elif user == 'paper' and compy == 'rock':
        print('paper vs. rock! paper wins!')

    elif user == 'paper' and compy == 'scissors':
        print('paper vs. scissors! scissors wins.')

    elif user == 'paper' and compy == 'spock':
        print('paper vs. spock! spock wins!')

    elif user == 'scissors' and compy == 'paper':
        print('paper vs. paper! it is a tie.')

    elif user == 'scissors' and compy == 'rock':
        print('scissors vs. rock! rock wins!')

    elif user == 'scissors' and compy == 'spock':
        print('scissors vs. spock! spock wins!')

    play_again = input('Do you want to play again?')
    if play_again == 'no':
        break
