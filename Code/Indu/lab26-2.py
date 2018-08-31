import random
import colorama

'''Animal capture'''
print("Some dangerous animals broke out of Portland zoo and hiding in Forst park. Help animal control to tranquilize and bring them back ")

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character
animals = ['🐺','🦁','🐘','🐒','🦍']

class Animal(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, random.choice(animals))


class Rescue(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '👧')

# Forest class

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
                    print('🌳 ', end='')
            print()



board = Board(15, 10)

pi, pj = board.random_location()
rescue = Rescue(pi, pj)

entities = [rescue]
animals = []

for i in range(10):
    ei, ej = board.random_location()
    animals = Animal(ei, ej)
    entities.append(animal)
    enemies.append(animals)


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
            print('you are in danger!')
            action = input('what will you do? ')
            if action == 'tranquilizer gun':
                print('The wild animal will sleep for next 4 hours. You are saved')
                entities.remove(enemy)
                enemies.remove(enemy)
                break
            else:
                print('you hestitated and killed')
                exit()


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)



