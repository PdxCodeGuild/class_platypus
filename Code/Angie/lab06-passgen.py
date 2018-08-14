import string
import random

x = ''
for i in range(10):
    c = random.choice(string.printable + string.digits)
    print(x)
    x = x + c
print(x)

# 'string builder pattern'

#passwords = []
#for x in passwords:
#    x += random.choice(string.printable + string.digits)
 #   x += str(1)
#print(x)