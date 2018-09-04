import re

with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read()  # book is opened
regex = '\w+'
#print(re.findall(regex, contents))
contents = contents.lower()
# find the number of words
content_length = len(contents)
character = contents.replace(' ', '')
num_character = len(character)

print(content_length)
# find the number of characters
    # remove all white space and count the characters
# find the number of sentences

# score = 4.71 * (num_character / content_length) + float(0.5)(content_length / sentences) - float(21.43)