import random


class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character


class Enemy(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🔥')


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👨‍🚒')

class Fountain(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '⛲️')

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



board = Board(15, 15)

pi, pj = board.random_location()
player = Player(pi, pj)
water_level = 5

fountain = Fountain(3,6)

entities = [player, fountain]
enemies = []
waters = [fountain]

for i in range(10):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)

print('Welcome Fire Fighter')
while True:
    board.print(entities)
    print('Water Level: ', end='')
    for i in range(water_level):
        print('💧', end='')
    print()
    command = input('What is your command? ')  # get the command from the user

    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west', '\x1b[D']:
        player.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east', '\x1b[C']:
        player.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north', '\x1b[A']:
        player.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south', '\x1b[B']:
        player.location_i += 1  # move down

    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            print('You\'ve encountered a fire!')
            action = input('Press space bar to shoot fire hose! ')
            if action == ' ' and water_level >= 0:
                print('You faught the fire!')
                water_level -= 1
                entities.remove(enemy)
                enemies.remove(enemy)
                break
            else:
                print('You ran out of water and got burned!')
                exit()

    for water in waters:
        if fountain.location_i == player.location_i and fountain.location_j == player.location_j:
            print('You found a water source.')
            fill = input('Do you want to fill your hose? (Type "yes" or "no") ').lower()
            while (fill == 'yes' or fill == 'y') and water_level < 5:
                water_level += 1
                print('Water Level: ', end='')
                for i in range(water_level):
                    print('💧', end='')
                print()
                fill = input('Do you want to keep filling? (Type "yes" or "no") ').lower()


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)
