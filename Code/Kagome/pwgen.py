import random



chars = string.printable

password = ''
for i in range(10):
    password = password + random.choice(chars)

print(password)