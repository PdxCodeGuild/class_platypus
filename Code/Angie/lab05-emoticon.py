import random

eyes = ['8', ':', ';', 'X', '|']
nose = ['-', 'U', '=', 'c', '^']
mouth = ['D', 'P', ')', '(', 'O']

emoticon = random.choice(eyes) + random.choice(nose) + random.choice(mouth)

print(emoticon)