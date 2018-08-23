import random
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
# Randomly pick a word
random.shuffle(words)
picked = words.pop()
print(picked)

# Set up the board
guesses = 10
already_guessed = ''
board = ''
for i in range(len(picked)):
    board = board + '_ '
# Play the game
while guesses > 0:
    print(board)
    print('# of guesses remaining: ' + str(guesses))
    letter_guess = input('Guess a letter: ')
    if picked.find(letter_guess) == -1:
        already_guessed = already_guessed + letter_guess
        guesses -= 1
    else:
        board[picked.find(letter_guess)] = letter_guess
    print(board)


