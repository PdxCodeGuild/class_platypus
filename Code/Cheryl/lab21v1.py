#lab 21 version 1

#represents current directory
file.txt

#to open a file
f = open('Nietzsche.txt')  # open the file
contents = f.read()  # read the contents


# step 1- to lowercase
f = f.lower()

print(contents)

f.close()  # close the file