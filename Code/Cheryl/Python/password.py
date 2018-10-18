# Versions 1 and 2

import random
import string


ascii = string.ascii_letters

n = input('Enter the number of characters you would like your random password to be >  ')
n = int(n)
i = 0

print('You\'re new password is: ', end ="")

while i < n:
    letters = random.choice(ascii)
    for letter in letters:
        print(letter, end ="")
        i += 1



