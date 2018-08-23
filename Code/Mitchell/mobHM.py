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
    print('# of guesses remaining: ' + str(guesses))
    print('already guessed: ' + already_guessed)
    letter_guess = input('Guess a letter: ')
    if picked.find(letter_guess) == -1:
        already_guessed = already_guessed + letter_guess
        guesses -= 1
    else:
        board_spot = picked.find(letter_guess) * 2
        board = board[:board_spot] + letter_guess + board[board_spot+1:]
        other_spot = board_spot + 1
        while picked.find(letter_guess) * 2 != -1:
        #for other_spot in range(len(board)):
            other_spot = picked.find(letter_guess) * 2
            board = board[:other_spot] + letter_guess + board[other_spot + 1:]
    print(board)


