# random password generator
import random
import string

n = int(input("What is your desired length of password?"))
# The password should contain Upper case and lowercase letters ,special characters,numbers
password = ''
for i in range(0, n):
    password += random.choice(string.printable)

print(password)
