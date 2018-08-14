import string, random


x = ''
for i in range(18):
    c = random.choice(string.printable + string.digits)
    x = x + c
print(x)

