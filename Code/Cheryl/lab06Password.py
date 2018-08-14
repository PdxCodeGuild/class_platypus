import string
import random




#### attempt at asking user for lowercase, uppercase, and numbers

lowercase = input("Please enter the number of lowercase letters you would like your password to have:  ")
uppercase = input("Please enter the number uppercase letters you would like:  ")
digits = input("Please enter the number of numbers you would like:  ")
lowercase_int = int(lowercase)
uppercase_int = int(uppercase)
digits_int = int(digits)
num_chars = lowercase_int + uppercase_int + digits_int
lc_password = 0
uc_password = 0
dig_password = 0
x = ''

while lc_password < lowercase_int:
    x += random.choice(string.ascii_lowercase)
    lc_password += 1


while uc_password < uppercase_int:
    x += random.choice(string.ascii_uppercase)
    uc_password += 1

while dig_password < digits_int:
    x += random.choice(string.digits)
    dig_password += 1

#changes it to a list
x = list(x)
#randomly shuffles the list
random.shuffle(x)
#joins them back together
x = ''.join(x)
print(x)



#user's number
# i = int(input("Please enter the number of digits you would like your password to be. > "))

# #using a for loop
# x = ''
# print(f"Your random {i} digit password is: ")
# for password in range(i):
#     x += random.choice(string.ascii_letters + string.digits)
# print(x)


#
# #using while loop
# password = 0
# x = ''
# while password <= i:
#     x += random.choice(string.ascii_letters + string.digits)
#     password += 1
# print(x)