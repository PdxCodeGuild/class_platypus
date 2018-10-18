# version 3

import random
from random import shuffle
import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits

l = input('Enter the number of lowercase letters you would like your random password to have >  ')
l = int(l)


u = input('Enter the number of uppercase letters you would like your random password to have >  ')
u = int(u)

d = input('Enter the number of digits you would like your random password to have >  ')
d = int(d)

i = 0
passw = ''

print('You\'re random password is: ', end ="")

while i < l:
    letters = random.choice(lowercase)
    for letter in letters:
        password_first = letter
        i += 1
    passw += password_first

i = 0
while i < u:
    letters = random.choice(uppercase)
    for letter in letters:
        password_second = letter
        i += 1
    passw += password_second

i = 0
while i < d:
    letters = random.choice(digits)
    for letter in letters:
        password_third = letter
        i += 1
    passw += password_third



def shuffle_string(passw):
    chars = list(passw)
    random.shuffle(chars)
    return ''.join(chars)

print(shuffle_string(passw))




# Versions 1 and 2
# import random
# import string
#
#
# ascii = string.ascii_letters
#
# n = input('Enter the number of characters you would like your random password to be >  ')
# n = int(n)
# i = 0
#
# print('You\'re new password is: ', end ="")
#
# while i < n:
#     letters = random.choice(ascii)
#     for letter in letters:
#         print(letter, end ="")
#         i += 1
#
#

