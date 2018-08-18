#
# Search the interwebs for an example Mad Lib
# Ask the user for each word you'll put in your Mad Lib
# Use string concatenation to put each word into the Mad Lib
# Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
# Add randomness! Use the random module, rather than selecting which adjective goes where in the story.
import random
welcome_mess = input("Thanks for visiting Cheryl's Mad Lib! Hit enter to play. ")

verbs = []
nouns = []
adjectives = []
names = []

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


print(verbs, names, nouns, adjectives)

print(f"Here's your Mad Lib! \nWhen {names[0]} starts to {random.choice(verbs)}\n with a {random.choice(adjectives)} {random.choice(nouns)}, {names[1]} \ncomes in and starts to {random.choice(verbs)} under the {random.choice(adjectives)} \n{random.choice(nouns)}. After all is said and\n {random.choice(verbs)}, the {random.choice(adjectives)} {random.choice(nouns)} \ntakes a nice, long {random.choice(verbs)}")

