import random
import colorama


width = 30  # the width of the board
height = 30  # the height of the board

# create a board with the given width and height
# we'll use a list of list to represent the board
board = []  # start with an empty list
for i in range(height):  # loop over the rows
    board.append([])  # append an empty row
    for j in range(width):  # loop over the columns
        board[i].append(' ')  # append an empty space to the board

# define the player position
player_i = 0
player_j = 0
# add random things on board
random_things = ['🐒','🦍','🦋','🌹']
danger = ['🐺','🦁','🐘' ]
for i in range(6):
    things_i = random.randint(0, height - 1)
    things_j = random.randint(0, width - 1)
    board[things_i][things_j] = random.choice(random_things)

# add 4 enemies in random locations
for i in range(10):
    enemy_i = random.randint(0, height - 1)
    enemy_j = random.randint(0, width - 1)
    board[enemy_i][enemy_j] = random.choice(danger)

# loop until the user says 'done' or dies
while True:

    command = input('where do you want to go? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command == '\x1b[D':
        player_j -= 1  # move left
    elif command == 'right':
        player_j += 1  # move right
    elif command == 'up':
        player_i -= 1  # move up
    elif command == 'down':
        player_i += 1  # move down

    # check if the player is on the same space as an enemy
    if board[player_i][player_j] == '§':
        print('you\'ve encountered an enemy!')
        action = input('what will you do? ')
        if action == 'attack':
            print('you\'ve slain the enemy')
            board[player_i][player_j] = ' '  # remove the enemy from the board
        else:
            print('you hestitated and were slain')
            break

            # print out the board
    for i in range(height):
        for j in range(width):
            # if we're at the player location, print the player icon
            if i == player_i and j == player_j:
                print('👧', end=' ')
            else:
                print(board[i][j], end=' ')  # otherwise print the board square
        print()