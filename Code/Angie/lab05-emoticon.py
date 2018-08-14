import random

emoticon = 0
while emoticon < 10:


    eyes = ['8', ':', ';', 'X', '|']
    nose = ['-', 'U', '=', 'c', '^']
    mouth = ['D', 'P', ')', '(', 'O']

    emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)

    print(emoticon)
    emoticon += 1
