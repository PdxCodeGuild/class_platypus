import re
# Opens and copies the text of a book's .txt file
with open('MobyDick.txt', 'r') as f:
    # Reads and saves the file to a string
    input_text = f.read()
f.close()
# Finds the number of characters (w/o spaces)
num_characters = len(input_text) - input_text.find(' ')
# Finds the number of words
num_words = len(re.compile('\w+').findall(input_text))
# Finds the number of sentences
end_sentence = '.!?'
num_sentences = 0
for i in range(len(input_text)):
    if input_text[i] in end_sentence:
        num_sentences += 1
print(f'Characters = {num_characters}, Words = {num_words}, Sentences = {num_sentences}')