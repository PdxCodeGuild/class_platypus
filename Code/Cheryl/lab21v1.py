#lab 21 version 1
import string

#to open a file
f = open('Nietzsche.txt', 'r')  # open the file
contents = (f.read()).lower() # read the contents and to lower

for p in string.punctuation:
    contents = contents.replace(p, ' ') #strips the punctuation

contents = contents.split() #puts all of the words into a list

print(len(contents)) #how many words are in the list

f.close()  # close the file