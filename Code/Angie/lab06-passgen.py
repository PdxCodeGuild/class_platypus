import string
import random

x = ''

while x <= str(10):
    x += random.choice(string.printable + string.digits)
    x += str(1)


# 'string builder pattern'
i = ''
for i in range(10):
   i += ''
print(i)

#passwords = []
#for x in passwords:
#    x += random.choice(string.printable + string.digits)
 #   x += str(1)
#print(x)