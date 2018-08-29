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
        self.strength = 1

    def big_enemy(self):
        super().__init__(location_i, location_j, '👾')
        self.health = 2
        self.strength = 2


class Player(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '😎')
        self.health = 5
        self.strength = 1


class Armor(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🛡️')


class Sword(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🗡️')


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
ai, aj = board.random_location()
si, sj = board.random_location()
player = Player(pi, pj)
armor = Armor(ai, aj)
sword = Sword(si, sj)
entities = [player, armor, sword]
enemies = []


for i in range(10):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)
with open('welcome.txt', 'r') as f:
    welcome = f.read()
with open('death.txt', 'r') as f:
    death = f.read()
# instructions
print("Move: L(left), R(right), U(up), D(down) Encounter: Attack, Flee")
print(welcome)
print('We all live in this cave. But some bad guys have tried to take it over.')
name = input(f" Thanks for agreeing to kill them all, but first what should I call you? ")
print('What do you mean you didn\'t bring armor? maybe you will find some in the cave.')


while True:

    board.print(entities)
    print(f' you have {player.health} health left.')

    command = input(f'{name}, what is your command? ')  # get the command from the user
# movement controls
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
# encounters
    for enemy in enemies:
        if armor.location_i == player.location_i and armor.location_j == player.location_j:
            player.health += 2
            entities.remove(armor)
            print('You found some armor. Your health went up!')
            break
        if sword.location_i == player.location_i and sword.location_j == player.location_j:
            player.strength += 1

        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            if action == 'attack':
                if random.randint(0, 1) == 0:
                    entities.remove(enemy)
                    enemies.remove(enemy)
                    break
                elif player.health > 0:
                    player.health -= enemy.strength
                    print('They got you.')
                    if player.health > 0:
                        fight = input(f'You have {player.health} left. Attack or flee?')
                        if fight == 'attack':
                            if random.randint(0, 1) == 0:
                                entities.remove(enemy)
                                enemies.remove(enemy)
                                break
                        else:
                            player.health -= 1
                            print(f'you ran but they got a swipe on you {player.health} left.')
                            break
                    else:
                        print(death)
                        print(f'thanks for trying {name} but your dead.')
                        exit()
            else:
                player.health -= 1
                print(f'you ran but they got a swipe on you {player.health} left.')
                break
#move enemy on board
    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)
