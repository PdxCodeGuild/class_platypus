import random

players = []
dice = {1: 'l', 2: 'r', 3: 'c', 4: '.',5: '.',6:  '.'}
pot = 0
while True:
    user_input = input(f" Enter player names. Enter done when done")
    if user_input == 'done':
        break
    else:
        user_input = players.append(user_input)
        continue
turns = 3
        for x in range(len(players)):
            if turns > 0:
                random.randint(0, 6):



