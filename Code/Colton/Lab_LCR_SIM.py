import random

players = []

while True:
    user_input = input(f" Enter player names. Enter done when done")
    if user_input == 'done':
        break
    else:
        user_input = players.append(user_input)
        continue
