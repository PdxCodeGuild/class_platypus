import random
import colorama
import chalk
import os

'''Animal capture'''

class Entity:
    def __init__(self, location_i, location_j, character):
        self.location_i = location_i
        self.location_j = location_j
        self.character = character

    def on_board(self, coord, board_range):
        while coord not in board_range:
            if coord > board_range[-1]:
                coord -= 1
            elif coord < board_range[0]:
                coord += 1

zoo_animals = ['🐺','🦁','🐘','🐒','🦍']

class Animal(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j,chalk.red(random.choice(zoo_animals)))


class Rescue(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, chalk.blue('👧'))

# Forest class

class Board:
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width), random.randint(0, self.height)

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
                    print(chalk.green('🌳'), end='')
            print()

board = Board()
pi,pj=(0,0)
#pi, pj = board.random_location()
rescue = Rescue(pi, pj)

entities = [rescue]
animals = []

for i in range(random.randint(5,10)):
    ei, ej = board.random_location()
    animal = Animal(ei, ej)
    entities.append(animal)
    animals.append(animal)


while True:

    board.print(entities)
    for animal in animals:
        print(animal.location_i, animal.location_j)
    print(chalk.bold('Some dangerous animals broke out of Portland zoo and hiding in Forst park. Help animal control to tranquilize and bring them back'))
    print(chalk.bold(len(animals)),'animals are out there')
    command = input('Whih direction do you want to move? l,r,u,d ')  # get the command from the user


    if command == 'done':
        break  # exit the game
    elif command in ['l', 'left', 'w', 'west','']:
        rescue.location_j -= 1  # move left
    elif command in ['r', 'right', 'e', 'east']:
        rescue.location_j += 1  # move right
    elif command in ['u', 'up', 'n', 'north']:
        rescue.location_i -= 1  # move up
    elif command in ['d', 'down', 's', 'south']:
        rescue.location_i += 1  # move down

    for animal in animals:
        if animal.location_i == rescue.location_i and animal.location_j == rescue.location_j:
            print('you got an animal!')
            action = input('Ready to use tranquilizer gun? y/n ')
            action=action.lower()
            if action in ['y','yes']:
                #os.system("dartsound.mp3")
                print(f'The wild animal will sleep for next 4 hours')
                entities.remove(animal)
                animals.remove(animal)

            else:
                print('you hestitated and eaten')
                exit()
    if len(animals) > 0:
        continue
    else:
        print("You have captured all animals")
        break

    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)



