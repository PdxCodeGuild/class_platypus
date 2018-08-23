#Hangman game with Indu and Angie

import random

def load_words(path):
    with open(path, 'r') as f:
        contents = f.read().split()  # read the contents and to lower
    words = []
    for i in range(len(contents)):
        if len(contents[i]) > 5:
            words.append(contents[i])
    return words


words = load_words('english.txt')
secret = random.choice(words)
print(secret)
secret = list(secret)
#print(secret)
print(f"The length of word you have to guess is {len(secret)}")
already_guessed = []
correct_letter = len(secret)*['_']
print(' '.join(correct_letter))
user_guess = input("Guess a letter?")
if user_guess in secret:
    index = index(user_guess in secret)
    print(index)









# hangman_pics = ['''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
# ./|\  |
#  / \  |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
# ./|\. |
#  / \  |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
# ./|\. |
# ./ \  |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
# ./|\. |
# ./ \. |
#       |
# =========''']
#
#
#
#
#
#
