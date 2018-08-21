
with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
    contents = f.read()
    # def words_in_text():
    #     with open('wright_brothers.txt', 'r', encoding='utf-8') as f:
    #         contents = f.read()
    #     contents = contents.lower()
    #     punctuation = "/[-[\]{}()*+?.,\\^$|#\s]/g, \"\\$&"
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
    punctuation = "/[-[\]{}()*+?.,\\^$|#\s]/g, \"\\$& "
    for char in punctuation:
        contents = contents.replace(char, '')
    contents = list(contents)
    print(contents)
    count = 0
    for char in range(len(contents)):
        count += 1
    return count


# sentences in a text
# import re
# contents = contents.lower()
# punctuation = "/[-[\]{}()*+?.,\\^$|#\s]/g, \"\\$&"
# for char in punctuation:
#     contents = contents.replace(char, ' ')
# contents = re.split(r' *[\.\?!][\'"\)\]]* *', contents)
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
#    print(words[i])