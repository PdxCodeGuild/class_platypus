import re

with open('book.txt', 'r', encoding='utf-8') as f:
    contents = f.read()  # book is opened
regex = '#[0-9a-fA-F]{6}'
print(re.findall(regex, contents))
contents = contents.lower()

# find the number of words
# find the number of characters
# find the number of sentences

# score = 4.71 * (chars / words) + float(0.5)(words / sentences) - float(21.43)