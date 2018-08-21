
import re
import string

# def words_in_text():
#     with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
#         contents = f.read()
#     contents = contents.lower()
#     punctuation = "/[-[\]{}()*+?.,\\^$|#\]/, \"\\$&"
#     for char in punctuation:
#         contents = contents.replace(char, ' ')
#     contents = contents.split()
#     count = 0
#     for word in range(len(contents)):
#         count += 1
#     return count
#
#
#
# characters in text
def char_in_text():
    with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
        contents = f.read()
    contents = contents.lower()
    contents = list(contents)
    for word in range(len(contents)):
        if contents[word] == string.ascii_lowercase:
            contents.append(word)
        else:
            contents.remove(word)
    print(contents)
    contents = list(contents)
    return len(contents)
print(char_in_text())

# #sentences in a text
# def sentences_in_text():
#     with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
#         contents = f.read()
#     contents = contents.lower()
#     punctuation = "/[-[\]{}()*+,^$|#\]/,\"$&"
#     for char in punctuation:
#         contents = contents.replace(char, ' ')
#     for x in contents:
#         words = re.split('[]', x)
#         for word in words:
#             doclist.append(word)
#     count = 0
#     for char in range(len(contents)):
#         count += 1
#     return count



# print(f" {4.71 *(char_in_text/ words_in_text) + .5(words_in_text / sentences_in_text) - 21.43}")