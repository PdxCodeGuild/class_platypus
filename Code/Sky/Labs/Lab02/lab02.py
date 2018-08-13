#Madlibs
#By Skyler Parker
#Created on 13AUG18

i = 0

while i == 0:
    adjectiveList = input('Please enter a list of 2 adjectives separated by commas only ')
    adjectiveA, adjectiveB = adjectiveList.split(',')
    animalList = input('Please enter a list of 2 animals separated by commas only ')
    animalA, animalB = animalList.split(',')
    placeA = input('Please enter the name of a place ')
    verbList = input('Please enter a list of 2 verbs separated by commas only ')
    verbA, verbB = verbList.split(',')
    print('There once was a ' + animalA + ' that could be described as ' + adjectiveA + '. '
          'One day the ' + animalA + ' decided to go to the ' + placeA + '. While ' + verbA + ' a ' + adjectiveB + ' ' + animalB + ' approached'
          ' the ' + animalA + ' and ' + verbB + ' towards the ' + animalA + '.')








