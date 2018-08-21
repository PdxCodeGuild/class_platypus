
with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
# find words in text
# contents = contents.lower()
# punctuation = ['.', '(', ')', "'", '!', '@', '#', '-', ';', '/', ':', '$', '%', '^', '&', '*', '_', '`', '?', '"', ',', '\n', '\\', '’', '“', '”',]
# for char in punctuation:
#     contents = contents.replace(char, ' ')
# contents = contents.split()
# print(contents)
# word_dict = {}
# for i in range(len(contents)):
#     if contents[i] not in word_dict:
#         word_dict[contents[i]] = 1
#     else:
#         word_dict[contents[i]] += 1
# words = list(word_dict.items())
# words.sort(key=lambda tup: tup[1], reverse=True)
# for i in range(min(10, len(words))):
#     print(words[i])




# characters in text
def char_in_text
    contents = contents.lower()
    punctuation = ['.', '(', ')', "'", '!', '@', '#', '-', ';', '/', ':', '$', '%', '^', '&', '*', '_', '`', '?', '"', ',', '\n', '\\', '’', '“', '”',' ']
    for char in punctuation:
        contents = contents.replace(char, '')
    word_dict = {}
    for i in range(len(contents)):
        if contents[i] not in word_dict:
            word_dict[contents[i]] = 1
        else:
            word_dict[contents[i]] += 1
    words = list(word_dict.items())
    words.sort(key=lambda tup: tup[1], reverse=True)
    for i in range(min(10, len(words))):
        return words[i]
