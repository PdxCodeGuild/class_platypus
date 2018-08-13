# Magic Eight Ball
# By Skyler Parker
# Created on 13AUG18

firstMessage = '''                                                                                                       
 \  / _  ._ |_   _. | |       _.  _ |    ._ _   _     _.    _.      _   _ _|_ o  _  ._     _. ._   _| 
  \/ (/_ |  |_) (_| | | \/   (_| _> |<   | | | (/_   (_|   (_| |_| (/_ _>  |_ | (_) | |   (_| | | (_| 
                        /                                    |                                       
                                    _                 
  _ |_   _. |   _    _|_ |_   _    (_) __ |_   _. | | 
 _> | | (_| |< (/_    |_ | | (/_   (_)    |_) (_| | | 
                                                             
                                                    '''

print(firstMessage)
import random

appExit = False

while appExit != bool(True):
    menuAnswer = int(input('\nMenu:\n\n1 - Shake the 8-ball\n2 - Close Program'))

    if menuAnswer == 1:

        # Declare Variables
        possibleAnswers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may '
                                                                                                       'rely on it',
                           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes',
                           'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now',
                           'Concentrate and ask again', 'Don\'t count on it', 'My reply is no', 'My sources say no',
                           'Outlook not so good', 'Very doubtful]']

        print('')
        print('\n*****' + (random.choice(possibleAnswers)) + '*****')

    else:
        appExit = True

