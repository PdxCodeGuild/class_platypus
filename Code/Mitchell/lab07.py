import string
import random
#Opening prompt ask which gamemode player wants
print('Do you want to play classic rock, paper, scissors, or an enhanced version with the addition of Spock and Lizard?')
gameType = input('Type ether "classic" for just rock, paper, scissors, or "enhanced" to add lizard and Spock:')
if gameType != 'classic' or gameType != 'enhanced':
    print('ERROR: You did not type ether "classic" or "enhanced".')
playAgain = 'yes'
#The states for "classic" rock, paper, scissors
while playAgain == 'yes' and gameType == 'classic':
    options = ['rock', 'paper', 'scissors']
    humanChoice = input('Which one will you pick? ("rock", "paper" or "scissors")')
    computerChoice = random.choice(options)
    #Tie outcome
    if humanChoice == computerChoice:
        print('I also chose ' + humanChoice + ', so it is a TIE!')
    #Human wins outcomes
    elif humanChoice == 'paper' and computerChoice == 'rock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'rock' and computerChoice == 'scissors':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'scissors' and computerChoice == 'paper':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
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

#The states for "enhanced" rock, paper, scissors, spock, lizard game
while playAgain == 'yes' and gameType == 'enhanced':
    options = ['rock', 'paper', 'scissors', 'lizard', 'Spock']
    humanChoice = input('Which one will you pick? ("rock", "paper", "scissors", "Spock" or "lizard")')
    computerChoice = random.choice(options)
    #Tie outcome
    if humanChoice == computerChoice:
        print('I also chose ' + humanChoice + ', so it is a TIE!')
    #Human wins outcomes
    elif humanChoice == 'paper' and computerChoice == 'rock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'paper' and computerChoice == 'Spock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'rock' and computerChoice == 'scissors':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'rock' and computerChoice == 'lizard':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'scissors' and computerChoice == 'paper':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'scissors' and computerChoice == 'lizard':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'Spock' and computerChoice == 'rock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'Spock' and computerChoice == 'scissors':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'lizard' and computerChoice == 'paper':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')
    elif humanChoice == 'lizard' and computerChoice == 'Spock':
        print('Dang! I chose ' + computerChoice + ', so you WIN because your ' + humanChoice + ' beats my ' + computerChoice + '!')

    #Computer wins outcomes
    elif computerChoice == 'paper' and humanChoice == 'rock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'paper' and humanChoice == 'Spock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'rock' and humanChoice == 'scissors':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'rock' and humanChoice == 'lizard':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'scissors' and humanChoice == 'paper':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'scissors' and humanChoice == 'lizard':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'Spock' and humanChoice == 'rock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'Spock' and humanChoice == 'scissors':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'lizard' and humanChoice == 'paper':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    elif computerChoice == 'lizard' and humanChoice == 'Spock':
        print('Sweet! I chose ' + computerChoice + ', so you LOSE because my ' + computerChoice + ' beats your ' + humanChoice + '!')
    else:
        print('ERROR: Please type ether "rock", "paper", "scissors", "Spock" or "lizard".')
    playAgain = input('Do you want to play again? (Type "yes" or "no")')
