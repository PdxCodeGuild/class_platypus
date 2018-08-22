import string
with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
contents = contents.lower()
punctuation = ['.', '(', ')', "'", '!', '@', '#', '-', ';', '/', ':', '$', '%', '^', '&', '*', '_', '`', '?', '"', ',', '\n', '\\', '’', '“', '”',]
for char in punctuation:
    contents = contents.replace(char, ' ')
contents = contents.split()
word_dict = {}
for i in range(len(contents)):
    if contents[i] not in word_dict:
        word_dict[contents[i]] = 1
    else:
        word_dict[contents[i]] += 1
words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])





