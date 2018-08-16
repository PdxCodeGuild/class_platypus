
import random


answers = ['yes', 'no', 'maybe', 'never', 'probably', 'ask again']


keep_running = 'yes'
while keep_running == 'yes':
    input('ask a question: ')
    print(random.choice(answers))
    keep_running = input('ask another question? ')


while True:
    input('ask a question: ')
    print(random.choice(answers))
    if input('ask another question?') != 'yes':
        break


