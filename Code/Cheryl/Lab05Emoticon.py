import random

eye = ['B', 'P', 'O', '8', '%', '@']
nose = ['>', '<', '?', 'T', '~']
mouth = [']', '[', '{', '}', '(', ')']

# print(random.choice(eye) + random.choice(nose) + random.choice(mouth))
#


#using a while loop
i = 0
while i < 5:
    print(random.choice(eye) + random.choice(nose) + random.choice(mouth))
    i += 1
