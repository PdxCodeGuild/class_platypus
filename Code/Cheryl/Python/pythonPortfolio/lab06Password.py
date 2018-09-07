import string
import random

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


x = list(x)
random.shuffle(x)
x = ''.join(x)
print(x)

