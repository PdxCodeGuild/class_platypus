#lab 21 version 1


#to open a file
f = open('Nietzsche.txt', 'r')  # open the file
contents = (f.read()).lower() # read the contents and to lower

print(contents)
f.close()  # close the file