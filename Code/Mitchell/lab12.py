import random
theNum = str(random.randint(1,10))
legalGuesses = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
guessing = 'yes'
while guessing == 'yes':
    guessed = input('I am think of a number between 1 and 10, what do you think it is?')
    if int(guessed) == int(theNum):
        print('You got it! My number was ' + theNum + '!')
        guessing = 'no'
    elif int(guessed) > int(theNum):
        guessing = input('Nope, my number is lower than that. Guess again? (Type "yes" or "no")')
    elif int(guessed) < int(theNum):
        guessing = input('Nope, my number is higher than that. Guess again? (Type "yes" or "no")')
