#lab 21 version 1


#to open a file
f = open('Nietzsche.txt', 'r')  # open the file
contents = f.read()  # read the contents

#to lowercase
print(contents.lower())

f.close()  # close the file