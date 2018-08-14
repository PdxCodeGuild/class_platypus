import string
import random

#user's number
i = int(input("Please enter the number of digits you would like your password to be. > "))

# #using a for loop
# x = ''
# print(f"Your random {i} digit password is: ")
# for password in range(i):
#     x += random.choice(string.ascii_letters + string.digits)
# print(x)



#using while loop
password = 0
x = ''
while password <= i:
    x += random.choice(string.ascii_letters + string.digits)
    password += 1
print(x)
