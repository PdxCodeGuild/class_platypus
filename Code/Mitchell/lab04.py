import random
print('Ask the Magic 8 Ball a yes or no question by typing it then pressing enter:')
notNeeded = input()
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'Most likely',
           'Yes', 'Ask again later',  'Reply hazy try again', 'Don\'t count on it', 'My reply is no', 'Very doubtful', 'No']
print(random.choice(answers))