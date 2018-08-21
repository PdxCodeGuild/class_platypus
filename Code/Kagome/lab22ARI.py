
filename = "1338.txt.utf-8.txt"
with open(filename, "r") as file:
    text = file.read()
wordcount = {}
for word in text.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(wordcount)

text = text.lower()
print(text)




#dont count each word. count total of words... so write the code for that! len(list)

# counts = {
#     'words': text,
#     'char_cnt': float(char_count),
#     'word_cnt': float(word_count),
#     'sentence_cnt': float(sentence_count)
#}
#
#
#
# def ari_read():
#     if word_cnt > 0.0:
#         score = (4.71 * ['char_cnt'] / ['word_cnt'] + 0.5 * (['word_cnt'] / ['sentence_cnt'] - 21.43))
#     return score