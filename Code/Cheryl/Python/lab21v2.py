#lab 21 version 2


import string

#to open a file
f = open('Nietzsche.txt', 'r')  # open the file
contents = (f.read()).lower() # read the contents and to lower

for p in string.punctuation:
    contents = contents.replace(p, ' ') #strips the punctuation

contents = contents.split() #puts all of the words into a list

contents_length = len(contents) #how many words are in the list


word_dict = {}

for word in contents:
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

print(word_dict)

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])

#pairs of words


f.close()  # close the file

