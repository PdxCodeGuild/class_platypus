#Lab 2, Mad Lib, with randomness and user choices

import random
welcome_mess = input("Thanks for visiting Cheryl's Mad Lib \nwhere your input will rewrite a famous \nGeorge Orwell quote! \nHit enter to play. ")

verbs = []
nouns = []
adjectives = []
names = []

#to see if I can get a list item to append itself into three different list items
for verb in verbs:
    if verb[0] == ',':
        print("* " + verb)
##############################

verbs.append(input("Please enter a verb. >    "))
verbs.append(input("Please enter another verb. >    "))
verbs.append(input("Please enter a last verb. >    "))

nouns.append(input("Please enter a noun. >    "))
nouns.append(input("Please enter another noun. >    "))
nouns.append(input("Please enter a last noun. >    "))

adjectives.append(input("Please enter an adjective. >    "))
adjectives.append(input("Please enter another adjective. >    "))
adjectives.append(input("Please enter a last adjective. >    "))

names.append(input("Please enter a name. >    "))
names.append(input("Please enter another name. >    "))


# {random.choice(verbs)}
# story = random.randint(1, 3)
story = 2
if story == 1:
    print(f'\n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}. \n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}. \n{random.choice(nouns)} {random.choice(verbs)} {random.choice(nouns)}.\n-- {names[0]}\n\nWar is peace. \nFreedom is slavery. \nIgnorance is strength.\n-- George Orwell')

elif story == 2:
    print(f'The very concept of \n{random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} fading \nout of the {random.choice(nouns)}. \n{random.choice(verbs)} will pass into {random.choice(nouns)}.\n-- {names[1]}\n\nThe very concept of \nobjective truth is fading \nout of the world. \nLies will pass into history.\n-- George Orwell')

else:
    print('All animals are equal, \nbut some animals are more \nequal than others.\n-- George Orwell')


