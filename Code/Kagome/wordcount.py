filename = "1338.txt.utf-8.txt"
file = open("1338.txt.utf-8.txt","r")
Text = file.read()
wordcount={}
for word in Text.split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print(wordcount)
file.close()




punc_list = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\""]
no_punc = ''
for i in punc_list:
    if i not in punc_list:
        no_punc += i
    else:
        no_punc += ' '







# Text = Text.lower()
Text = Text.split()
print(Text)







# Counter
# Counter(text).most_common()
# Text = list(word_dict.items())  # .items() returns a list of tuples
# text.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count