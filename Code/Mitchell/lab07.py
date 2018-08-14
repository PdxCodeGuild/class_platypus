import string
import random
options = ['rock', 'paper', 'scissors']
print('If you want play rock, paper, scissors, type ether "rock", "paper" or "scissors", then wait for my pick.')
playAgain = 'yes'
while playAgain == 'yes':
    humanChoice = input('Which one will you pick? ("rock", "paper" or "scissors")')
    computerChoice = random.choice(options)
    #Tie outcome
    if humanChoice == computerChoice:
        print('I also chose ' + humanChoice + ', so it is a TIE!')
    #Human wins outcomes
    elif humanChoice == 'paper' and computerChoice == 'rock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'rock' and computerChoice == 'scissors':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'scissors' and computerChoice == 'paper':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
    #Computer wins outcomes
    elif computerChoice == 'paper' and humanChoice == 'rock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'rock' and humanChoice == 'scissors':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'scissors' and humanChoice == 'paper':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    else:
        print('ERROR: Please type ether "rock", "paper" or "scissors')
    playAgain = input('Do you want to play again? (Type "yes" or "no")')
