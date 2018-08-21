import re
punctuation = '.,!?()\'"-;:'
word_count = {}
#Opens and copies the text of a book's .txt file
with open('MobyDick.txt', 'r') as f:
    #Reads the file and converts it to lowercase
    input_file = f.read().lower()
    #Strips punctuation and stores words in list
    word_list = re.compile('\w+').findall(input_file)
    for i in range(len(word_list)):
        #If the word is not in the dictionary add it
        if word_list[i] not in word_count:
            word_count[word_list[i]] = 1
        #If its in the dictionary incriment the count
        else:
            word_count[word_list[i]] += 1
print(word_count)