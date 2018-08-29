import random
from termcolor import colored
import time

from colorama import Fore, Back, Style

def style_files(path):
    with open(path, 'r') as f:
        # print(Style.DIM)
        print(Fore.YELLOW + Back.LIGHTBLACK_EX)
        return f.read()


print(style_files('title.txt'))
print(Style.RESET_ALL)
print(Back.LIGHTBLACK_EX)

#write out the rules of the game.
#1. after attacking and killing a cube, add 10 points
#2. find a way to get health (5 points each time_
#3. every random time you attack, you get points taken away 5 points
#4. when you win, by clearing the board, have something happen
#5. havesomething happen when you lose.


#Choose your race: Klingon or Federation
user_race = input('Choose your race: Klingon or Federation. >   ').upper()
if user_race == 'KLINGON':
    print(style_files('klingon.txt') + '\n\n\tYou chose to be a Klingon! \n\n')
else:
    print(style_files('federation.txt') + '\n\n\tYou chose to be a member of the Federation! \n\n')

time.sleep(3)

#Choose your enemy: Romulan or Borg
user_enemy = input('\nChoose your enemy: Romulan or Borg. >   \n\n').upper()

if user_enemy == 'BORG':
    print(style_files('borg.txt') + '\n\n\tYou chose to fight the Borg! \n\n')
else:
    print(style_files('romulan.txt') + '\n\n\tYou chose to fight the Romulans! \n\n')

time.sleep(2)
##############
class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        if user_enemy == "BORG":
            super().__init__(location_i, location_j, '🕋') #borg
        else:
            super().__init__(location_i, location_j, '👿') #romulan


class Player(Entity):
    def __init__(self, location_i, location_j):
        if user_race == "KLINGON":
            super().__init__(location_i, location_j, '👹') #klingon
        else:
            super().__init__(location_i, location_j, '👽') #federation


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    def __getitem__(self, j):
        return self.board[j]

    def print(self, entities):
        for i in range(self.height):
            for j in range(self.width):
                for k in range(len(entities)):
                    if entities[k].location_i == i and entities[k].location_j == j:
                        print(entities[k].character, end='')
                        break
                else:
                    print(' ', end='')
            print()



board = Board(10, 10)

pi, pj = board.random_location()
player = Player(pi, pj)

entities = [player]
enemies = []

for i in range(10):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)


while True:

    board.print(entities)

    command = input('what is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        player.location_i += 1  # move down

    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                print('you\'ve slain the enemy')
                time.sleep(1.5)
                entities.remove(enemy)
                enemies.remove(enemy)
                break
            else:
                print('you hestitated and were slain')
                if user_enemy == "BORG":
                    print('You have been assimilated.')
                    time.sleep(3)
                    print(style_files('borg.txt') + '\t\tYou are now Borg...')
                else:
                    if user_race == 'KLINGON':
                        print(style_files('romulan.txt') + '\t\tYou have been put in a Romulan Prison Camp where you will die a slow and dishonorable death.')
                    else:
                        print(style_files('romulan.text') + 'test')

                exit()


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)
