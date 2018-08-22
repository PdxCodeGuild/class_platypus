
# Open the file.
with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read()

contents = contents.lower()

# define a punctuation string
punctuation = ['.', '(', ')', "'", '!', '@', '#', '-', ';', '/', ':', '$', '%', '^', '&', '*', '_', '`', '?', '"', ',', '\n', '\\', '’', '“', '”',]

# iterate over the characters of the punctuation string
for char in punctuation:
    contents = contents.replace(char, ' ')  # replace each punctuation character in contents with a space
# this will look like {'the':34, 'hello', 20, ...}
word_dict = {}
contents = contents.split(' ')
for word in contents:
    if word in word_dict:
        word_dict[word] += 1
    else:
        # add to key value
        word_dict[word] = 1
#print(word_dict)

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items())  # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(11, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])











# Make everything lowercase, strip punctuation, split into a list of words.
# Your dictionary will have words as keys and counts as values. If a word isn't in your dictionary yet, add it with a count of 1. If it is, increment its count.
# Print the most frequent top 10 out with their counts. You can do that with the code below.

