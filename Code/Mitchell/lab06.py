import string
import random

characters = (string.ascii_letters + string.digits + string.printable)
length = input('How many characters do you want your password to be?')
start = 0
while start < int(length):
 print(random.choice(characters), end='')
 start = start + 1