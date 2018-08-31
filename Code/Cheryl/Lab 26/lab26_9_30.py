#ST audio files from http://www.trekcore.com/audio/
#extra emojis ☄️

import random

from termcolor import colored
import time

from colorama import Fore, Back, Style
import pygame
import time

def audio(audio_file):
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.Sound(audio_file)
    sounda.play()
    time.sleep(3)

audio("st_audio/tos_bridge_1_activate.wav")

def end_credits(audio):
    audio('st_audio/credits.wav')
    time.sleep(44)

def style_files(path):
    with open(path, 'r') as f:
        # print(Style.DIM)
        print(Fore.YELLOW + Back.LIGHTBLACK_EX)
        return f.read()


print(style_files('title.txt'))
print(Style.RESET_ALL)
print(Back.LIGHTBLACK_EX)


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
            super().__init__(location_i, location_j, '🖖') #federation


class Shield(Entity):
    def __init__(self, location_i, location_j):
        super().__init__(location_i, location_j, '🌟') #shield

print(Fore.BLACK + Back.CYAN)
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def random_location(self):
        return random.randint(0, self.width - 1), random.randint(0, self.height - 1)

    # Returns a random location on the board
    def random_location_safe(self, entities):
        while True:
            location_i = random.randint(0, self.width - 1)
            location_j = random.randint(0, self.height - 1)
            for entity in entities:
                if entity.location_i == location_i and entity.location_j == location_j:
                    break
            else:
                break
        return location_i, location_j

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
shields = []

for i in range(10):
    ei, ej = board.random_location()
    enemy = Enemy(ei, ej)
    entities.append(enemy)
    enemies.append(enemy)

for i in range(3):
    ei, ej = board.random_location()
    shield = Shield(ei, ej)
    entities.append(shield)
    shields.append(shield)


#sets points for game
points = 0
# shield_points = 0
new_points = points
# new_points = points + shield_points
enemy_count = 0


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

    for shield in shields:
        if shield.location_i == player.location_i and shield.location_j == player.location_j:
            print('you\'re shields are at full power.')
            time.sleep(2)
            new_points += 5
            # print(shield_points)
            entities.remove(shield)
            shields.remove(shield)
            break
            time.sleep(3)


    for enemy in enemies:
        if enemy.location_i == player.location_i and enemy.location_j == player.location_j:
            proximity_fire_audio = ["st_audio/phasersready.wav", 'st_audio/tactalertvesselapproach.wav']
            random_proximity_fire_audio = random.choice(proximity_fire_audio)
            audio(random_proximity_fire_audio)
            print('you\'ve encountered an enemy!')
            action = input('what will you do? ')
            # enemy_count = 0
            if action == 'fire':
                enemy_count += 1
                #adds random weapon sounds on fire
                fire_audio = ["st_audio/tng_weapons.wav", "st_audio/tos_photon_torpedo.wav", "st_audio/tng_torpedo.wav", "st_audio/tng_torpedo2.wav", "st_audio/tng_torpedo3.wav"]
                random_fire_audio = random.choice(fire_audio)
                audio(random_fire_audio)
                print(enemy_count)
                if enemy_count == 10:
                    print('You\'ve won the game! ')
                    if user_race == 'KLINGON':
                        audio('st_audio/largeexplosion.wav')
                        print(style_files('klingon_ship.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_two.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_three.txt'))
                        time.sleep(0.25)
                        print(style_files('klingon_ship_four.txt'))
                        end_credits(audio)
                        exit()
                    else:
                        audio('st_audio/livelong.wav')
                        print(style_files('federation_ship.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_two.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_three.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_four.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_five.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_six.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_seven.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_eight.txt'))
                        time.sleep(0.25)
                        print(style_files('federation_ship_nine.txt'))
                        time.sleep(0.25)
                        print(f"\n\n\n\n{style_files('federation_ship_ten.txt')}")
                        end_credits(audio)
                        exit()

                #adds points or deducts random points based on who wins the attack
                # win_lose = 'WIN'
                win_lose = ['WIN', 'LOSE']
                win_lose = random.choice(win_lose)
                if win_lose == 'LOSE':
                    print('You\'ve lost the fight. ')
                    new_points -= 5
                    print(f'You now have: {new_points} points')
                    if new_points == 10:
                        audio('st_audio/primaryshieldsfailing.wav')
                    elif new_points == 5:
                        audio('st_audio/lifesupportfailureabandon.wav')
                    if new_points <= 0:
                    # IF YOU LOSE
                        audio('st_audio/largeexplosion.wav')
                        if user_enemy == "BORG":
                            print('You have been assimilated.')
                            time.sleep(3)
                            print(style_files('borg.txt') + '\t\tYou are now Borg...')
                            end_credits(audio)
                        else:
                            if user_race == 'KLINGON':
                                print(style_files(
                                    'romulan.txt') + '\t\tYou have been put in a Romulan Prison Camp where you will die a slow and dishonorable death.')
                                end_credits(audio)
                            else:
                                print(style_files('romulan.text') + 'test')
                                end_credits(audio)
                        end_credits(audio)
                        exit()

                else:
                    print('you\'ve destroyed their ship!')
                    new_points += 5
                    print(f'You now have: {new_points} points')

                time.sleep(1.5)
                entities.remove(enemy)
                enemies.remove(enemy)
                break

            # elif enemy_count == 0:
            #     print('WORKING')
            else:
                print('You misfired and your ship has been destroyed.')
                if user_enemy == "BORG":
                    print('You have been assimilated.')
                    time.sleep(3)
                    print(style_files('borg.txt') + '\t\tYou are now Borg...')
                    end_credits(audio)
                else:
                    if user_race == 'KLINGON':
                        print(style_files('romulan.txt') + '\t\tYou have been put in a Romulan Prison Camp where you will die a slow and dishonorable death.')
                    else:
                        print(style_files('romulan.txt'))
                        end_credits(audio)
                end_credits(audio)
                exit()


    # for enemy in enemies:
    #     if random.randint(0, 1) == 0:
    #         enemy.location_i += random.randint(-1, 1)
    #     else:
    #         enemy.location_j += random.randint(-1, 1)