import random
dice = 'LCR...'
center = 0
# User enters player's names into dictionary with 3 chips each
name = input('Welcome to LCR Simulator, please enter the name of a the first player: ')
players = [name]
while name != 'done':
    name = input('Enter another player\'s name or type "done" if all players are entered: ')
    if name == 'done':
        break
    else:
        players.append(name)
# Each player starts with 3 chips
chips = [3] * len(players)
playing = True
# Loops while game is going on
while playing:
    # Go through list of players giving each a turn
    for i in range(len(players)):
        # Checks if there is a winner if so end
        if chips[i] + center == len(chips) * 3:
            print(players[i] + ' won this game of LCR!')
            exit()
        print(f'On {players[i]}\'s turn they started with {chips[i]} and rolled: (', end='')
        # Rolls the # of dice equal to their # of chips
        for j in range(chips[i]):
            die = dice[random.randint(0, 5)]
            print(die, end=' ')
            # If a L is rolled, give chip to player on left
            if die == 'L':
                left_spot = len(chips) - 1 - i
                chips[i] -= 1
                chips[left_spot] += 1
            # If a C is rolled, put a chip in the center
            elif die == 'C':
                chips[i] -= 1
                center += 1
            # If a R is rolled, give a chip to player on right
            elif die == 'R':
                chips[i] -= 1
                # If last spot in array pass chip to first spot
                if i + 1 == len(chips):
                    chips[0] += 1
                # Otherwise pass the chip to player to right
                else:
                    chips[i+1] += 1
        print(f'). Ending their turn with {chips[i]} chips.')