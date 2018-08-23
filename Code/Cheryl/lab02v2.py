#Lab 2, Mad Lib, with randomness and user choices

import random

welcome_mess = input("Thanks for visiting Cheryl's Mad Lib \nwhere your input will rewrite a famous \nGeorge Orwell quote! \nHit enter to play. ")

verbs = input("Please enter three verbs separated by a space. >   ").split()
nouns = input('Please enter three nouns separated by a space. >   ').split()
adjectives = input('Please enter three adjectives separated by a space. >   ').split()
names = input('Please enter three names separated by a space. >   ').split()

story = random.randint(1, 3)

if story == 1:
    print(f'\n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}. \n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}. \n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}.\n-- {random.choice(names)}\n\nWar is peace. \nFreedom is slavery. \nIgnorance is strength.\n-- George Orwell')

elif story == 2:
    print(f'The very concept of \n{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} fading \nout of the {random.choice(nouns)}. \n{random.choice(verbs)} will pass into {random.choice(nouns)}.\n-- {random.choice(names)}\n\nThe very concept of \nobjective truth is fading \nout of the world. \nLies will pass into history.\n-- George Orwell')

else:
    print(f'{random.choice(adjectives)} {random.choice(nouns)} are {random.choice(nouns)}, \nbut some {random.choice(adjectives)} {random.choice(verbs)} {random.choice(adjectives)} \n{random.choice(nouns)} than others.\n-- {random.choice(names)}\n\nAll animals are equal, \nbut some animals are more \nequal than others.\n-- George Orwell')


