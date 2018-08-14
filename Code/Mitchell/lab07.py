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
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    #Human wins outcomes
    if humanChoice == 'paper' and computerChoice == 'rock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    if humanChoice == 'rock' and computerChoice == 'scissors':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    if humanChoice == 'scissors' and computerChoice == 'paper':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your' + humanChoice + ' beats my ' + computerChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    #Computer wins outcomes
    if computerChoice == 'paper' and humanChoice == 'rock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    if computerChoice == 'rock' and humanChoice == 'scissors':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
    if computerChoice == 'scissors' and humanChoice == 'paper':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
        playAgain = input('Do you want to play again? (Type "yes" or "no")')
