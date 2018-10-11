
import string


f = open('Nietzsche.txt', 'r')
contents = (f.read()).lower()

for p in string.punctuation:
    contents = contents.replace(p, ' ')

contents = contents.split()

contents_length = len(contents)

word_dict = {}

for word in contents:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)


words = list(word_dict.items())
words.sort(key=lambda tup: tup[1], reverse=True)
for i in range(min(10, len(words))):
    print(words[i])


f.close()

