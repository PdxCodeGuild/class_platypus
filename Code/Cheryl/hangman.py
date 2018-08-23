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
# secret = "hippopotamus"
print(secret)
secret = list(secret)
#print(secret)
print(f"The length of word you have to guess is {len(secret)}")
already_guessed = []
correct_letter = len(secret)*['_']
print(' '.join(correct_letter))
count = 0

hangman_pics = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \  |
      |
=========''', '''
  +---+
  |   |
  O   |
./|\. |
./ \. |
      |
=========''']

while True:
    user_guess = input("Guess a letter?  ")
    found_letter = False

    for i in range(len(secret)):
        if user_guess == secret[i]:
            found_letter = True
            correct_letter[i] = user_guess
            print(' '.join(correct_letter))
            already_guessed.append(user_guess)
    if correct_letter == secret:
        print("You win")
        break


    if not found_letter:
        count += 1
        if user_guess != secret[i]:
            already_guessed.append(user_guess)
            print(f"not a letter in the word. You have {10-count} guesses left. \n{already_guessed} \n{hangman_pics[count - 1]}")

            if count == 10:
                print('You lose')
                break

