import random
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
# Opens and copies the text of a book's .txt file
with open('english.txt', 'r') as f:
    input_text = f.read()
f.close()
words = list(input_text.split('\n'))
# Removes all words with less than 5 letters
i = 0
while i < len(words):
    if len(words[i]) < 5:
        words.remove(words[i])
    else:
        i += 1
# Playing the game, loops if plaid again
playing = True
while playing:
    won = False
    pic = 0
    # Randomly pick a word
    random.shuffle(words)
    picked = words.pop()
    # Set up the board
    guesses = 10
    already_guessed = ''
    board = ''
    # Initialize the board and pick word
    for i in range(len(picked)):
        board = board + '_ '
    # Loop until they player runs out of guesses
    while guesses > 0:
        print(hangman_pics[pic])
        print(board)
        print('# of guesses remaining: ' + str(guesses))
        print('already guessed: ' + already_guessed)
        # Checks if the player has won
        if board.find('_') == -1:
            won = True
            break
        letter_guess = input('Guess a letter: ').lower()
        # Loop through picked word, see if guest letter is in it
        for i in range(len(picked)):
            # If guessed letter is in word, replace '_' with it
            if picked[i] == letter_guess:
                i *= 2
                board = board[:i] + letter_guess + board[i + 1:]
            # If not in word, add it to already_guest and decrement guesses
            if picked.find(letter_guess) == -1:
                already_guessed = already_guessed + letter_guess + ', '
                guesses -= 1
                pic += 1
                break
    # Prints win/lose message and play again option
    if won == True:
        print('You won!')
    else:
        print(hangman_pics[10])
        print('You lost... The word was: ' + picked)
    play_again = input('Do you want to play again? (type "yes" or "no") ').lower()
    if play_again == 'no':
        playing = False