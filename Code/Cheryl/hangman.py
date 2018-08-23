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
# secret = random.choice(words)
secret = "hippopotamus"
print(secret)
#secret = list(secret)
#print(secret)
print(f"The length of word you have to guess is {len(secret)}")
already_guessed = []
correct_letter = len(secret)*['_']
print(' '.join(correct_letter))
user_guess = input("Guess a letter?")


while True:
    count=0
    if  user_guess in secret:
        word_index = secret.index(user_guess)
        print(word_index)
        correct_letter.insert(word_index,user_guess)
        print(' '.join(correct_letter))
        already_guessed.append(user_guess)
        secret[secret.index(user_guess) + 1:]
        # if user_guess in secret:

            # secret[secret.index_one(user_guess) + 1:].index_one(user_guess)
        # secret[secret.index(user_guess) + 1:].index(user_guess) + secret.index(user_guess) + 1

    else:

        count +=1
        print(f"not a letter in the word. You have {10-count} guesses left")







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
