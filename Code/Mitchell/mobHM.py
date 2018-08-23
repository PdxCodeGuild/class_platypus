import random
# Opens and copies the text of a book's .txt file
with open('english.txt', 'r') as f:
    input_text = f.read()
f.close()

words = list(input_text.split('\n'))
for i in range(len(words)):
    if len(words[i]) < 5:
        words.remove(words[i])
        continue
print(words)