import random
#Starting prompt to choose game mode
start = input('To play the Number Guessing Game type ether "think" if you want to think a number '
              'and I try and guess \nit or type "guess" if you want me to think of a number and you guess it:').lower()
#Computer thinks of a number and user guesses it
if start == 'guess':
    theNum = str(random.randint(1,10))
    guessing = 'yes'
    while guessing == 'yes':
        guessed = input('I am think of a number between 1 and 10, what do you think it is?')
        #User guessed computer's number
        if int(guessed) == int(theNum):
            print('You got it! My number was ' + theNum + '!')
            guessing = 'no'
        #User's guess was too high
        elif int(guessed) > int(theNum):
            guessing = input('Nope, my number is lower than that. Guess again? (Type "yes" or "no")').lower()
        #User's guess was too low
        elif int(guessed) < int(theNum):
            guessing = input('Nope, my number is higher than that. Guess again? (Type "yes" or "no")').lower()
#User thinks of a number and computer guesses it
elif start == 'think':
    input('Think of a number between 1 and 10, then press the Enter key when you have it.')
    thinking = 'yes'
    x = 1
    y = 10
    while thinking == 'yes':
        randomNum = str(random.randint(x, y))
        guess = input('Is it ' + randomNum + '? (Type ether "yes", "higher" or "lower")').lower()
        #Computer guest the user's number
        if guess == 'yes':
            print('Sweet I knew I could guess it!')
            thinking = 'no'
        #Computer's guess was too low
        elif guess == 'higher':
            x = int(randomNum) + 1
        # Computer's guess was too high
        elif guess == 'lower':
            y = int(randomNum) - 1
#Invalid game mode entered
else:
    print('ERROR: Invalid game mode as nether "guess" or "think" were entered.')
