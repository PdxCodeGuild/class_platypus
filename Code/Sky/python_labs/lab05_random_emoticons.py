# Random Emoticon Generator
# By Skyler Parker
# Created on 13AUG18

import random

appExit = False

while appExit != bool(True):
    menuAnswer = int(input('\nMenu:\n\n1 - Generate Random Emoticon\n2 - Close Program'))

    if menuAnswer == 1:

        # Declare Variables
        possibleLeftArm = ['', '<', '/', '\\', '']
        possibleRightArm = ['', 'ノ', '/', '>', '?']
        possibleLeftFace = ['', '(', '((', '{', '[']
        possibleRightFace = ['', ')', '))', '}', ']']
        possibleEye = ['', '^', '@', '*', '~', 'T']
        possibleMouth = ['', '_', 'o', 'O', '.', '#']

        print('')
        print('\n*****   ' + (random.choice(possibleLeftArm)) + (random.choice(possibleLeftFace))
              + (random.choice(possibleEye)) + (random.choice(possibleMouth))
              + (random.choice(possibleEye)) + (random.choice(possibleRightFace)) + (random.choice(possibleRightArm))
              + '   *****')

    else:
        appExit = True

