
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
quit_string = ''
while quit_string != 'quit': # game loop
    secret = random.choice(words)
    # secret = "hippopotamus"
    secret = list(secret)
    # print(secret)
    print(f"The length of word you have to guess is {len(secret)}")
    already_guessed = []
    correct_letter = len(secret) * ['_']
    count = 0
    while True: # turn
        print(' '.join(correct_letter))
        user_guess = input("Guess a letter?  ")
        if user_guess in already_guessed:
            print('You\'ve already tried this letter. ')
            continue

        found_letter = False

        for i in range(len(secret)):
            if user_guess == secret[i]:
                found_letter = True
                correct_letter[i] = user_guess
                already_guessed.append(user_guess)
        if correct_letter == secret:
            print(''.join(secret))
            print("You win")

            break

        if not found_letter:

            count += 1

            if user_guess != secret[i]:
                already_guessed.append(user_guess)
                print(f"not a letter in the word. You have {10-count} guesses left. \n{already_guessed} \n{hangman_pics[count - 1]}")

                if count == 10:
                    print(''.join(secret))
                    print('You lose')
                    # quit_string = input('Hit return to play again or type \'quit\' to leave the game. > ').lower()
                    break

    quit_string = input('Hit return to play again or type \'quit\' to leave the game. > ').lower()
    #ETAOIN SHRDLU CMFWYP VBGKQJ XZ