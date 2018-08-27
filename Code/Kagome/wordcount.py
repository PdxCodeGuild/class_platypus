filename = "1338.txt.utf-8.txt"
file = open(filename, "r")
text = file.read()
word_count = {}
pair_count = {}
for word in text.split():
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1
print(word_count)
file.close()



punc_list = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","'","\""]
no_punc = ''
for char in text:
    if char not in punc_list:
        no_punc += char
    else:
        no_punc += ' '

text = text.lower()
text = text.split()
print(text)
print(no_punc)

# {'the': 20, 'hello': 15, ...}


# Counter(Text).most_common()
# text = list(word_dict.items())  # .items() returns a list of tuples
# text.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count