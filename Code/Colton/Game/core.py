import random


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '😈')
        self.health = 1

class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '😎')
        self.health = 10

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
with open('welcome.txt', 'r') as f:
    welcome = f.read()
print(welcome)
print('We all live in this cave. But some bad guys have tried to take it over.')
name = input(f" Thanks for agreeing to do kill them all, but first what should I call you? ")
while True:

    board.print(entities)
    print(f' you have {player.health} health left.')

    command = input(f'{name}, what is your command? ')  # get the command from the user

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
                if random.randint(1, 1) == 0:
                    entities.remove(enemy)
                    enemies.remove(enemy)
                    break
                else:
                    while player.health > 0:
                        player.health -= 1
                        fight = input(f'You have {player.health} left. Attack or flee?').lower
                        if fight == 'attack':
                            if random.randint(0, 1) == 0:
                                entities.remove(enemy)
                                enemies.remove(enemy)
                                break
            else:
                print(f'you ran but they got a swipe on you {player.health} left.')
                break
#move enemy on board
    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)
