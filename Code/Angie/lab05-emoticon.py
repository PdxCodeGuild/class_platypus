import random

eyes = ['8', ':', ';', 'X', '|']
nose = ['-', 'U', '=', 'c', '^']
mouth = ['D', 'P', ')', '(', 'O']

c = 0

while c < 10:
    emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)
    c += 1

    if c == 11:
        break

    print(emoticon)





