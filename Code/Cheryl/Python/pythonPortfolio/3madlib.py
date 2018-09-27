#Lab 2, Mad Lib, with randomness and user choices

import random

welcome_mess = input("Thanks for visiting Cheryl's Mad Lib where your input will rewrite a famous, and quite mad, Donald Trump quote!\n \nHit enter to play. \n")

verbs = input("Please enter three verbs separated by a space. >   ").split()
nouns = input('Please enter three nouns separated by a space. >   ').split()
adjectives = input('Please enter three adjectives separated by a space. >   ').split()
adverbs = input('Please enter three adverbs separated by a space. >   ').split()



answer = 'yes'

while answer == 'yes':
    story = random.randint(1, 3)

    if story == 1:
        print(f'\n"I will be {random.choice(adjectives)} to the {random.choice(nouns)}. I mean, I {random.choice(verbs)} to help {random.choice(nouns)}."\n\n"I will be phenomenal to the women. I mean, I want to help women."\n\tFace the Nation, 9/8/15\n')

    elif story == 2:
        print(f'\n"It\'s {random.choice(adverbs)} {random.choice(adjectives)} outside, they are calling it a {random.choice(adverbs)} freeze, {random.choice(nouns)} ahead of normal. Man, we could use a {random.choice(adjectives)} {random.choice(adjectives)} dose of global warming!"\n\n"It\'s really cold outside, they are calling it a major freeze, weeks ahead of normal. Man, we could use a big fat dose of global warming!"\n\tTwitter, 19/10/15\n')

    else:
        print(f'\n"I\'m {random.choice(adjectives)}. Some people would say I\'m {random.choice(adverbs)}, {random.choice(adverbs)}, {random.choice(adverbs)} {random.choice(adjectives)}."\n\n"I\'m intelligent. Some people would say I\'m very, very, very intelligent."\n\tFortune, 3/4/00\n')

    answer = input('Would you like to play again? Type \'yes\' or \'no\' >   \n').lower()

input('\n\nThanks for playing!')


