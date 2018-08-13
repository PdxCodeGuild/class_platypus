import random
import time
print('Welcome to the Mysterious Magic 8 Ball online')
time.sleep(2)

answers = ['Not Yet','It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Do not count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']


while True:
    input('What is your question?\n:')
    print(random.choice(answers))

    quit_string = input('Please type quit\n:')
    if quit_string == 'quit':
        break