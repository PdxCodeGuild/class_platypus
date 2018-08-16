
import string
import random

print(string.ascii_letters)
print(string.printable)
print(string.digits)

print(random.choice(string.ascii_letters + string.digits))


# 'string builder pattern'
x = ''
for i in range(10):
    x += 'hi'
print(x)