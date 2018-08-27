#string.letters
filename = "1338.txt.utf-8.txt"
with open(filename, "r") as file:
    text = file.read()
word_count = {}
#word_count = (len(words)
# for word in text.split():
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1
# print(word_count)

text = text.lower()
print(text)

num_sentence = 0
end_punc = '.?!'
for i in range(len(text)):
    if text[i] in end_punc:
        num_sentence += 1


char_count = len(text) - text.count(' ')
word_count = len(text)
sentence_count = len(text)


#dont count each word. count total of words... so write the code for that! len(list)

counts = {
    'words': text,
    'char_cnt': float(char_count),
    'word_cnt': float(word_count),
    'sentence_cnt': float(sentence_count)
}

print(f'Characters = {char_count}, Words = {word_count}, Sentences = {sentence_count}')




def ari_read(word_cnt):
    if word_cnt > 0.0:
        score = (4.71 * 'float(char_cnt)' / 'word_cnt') + 0.5 * (['word_cnt'] / ['sentence_cnt'] - 21.43))
    return score

ari_read(word_count)