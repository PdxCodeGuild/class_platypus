import string
import random

password_in = input("Need a password? ")
length = int(input("How long does it need to be? "))
# lower = int(input("How many lowercase letters? "))
# upper = int(input("How many uppercase letters? "))
# digit = int(input("How many numbers do you need? "))
# punc = int(input("How many special characters?"))

for i in range(length):
    random_password = (random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation))
    random_password = list(random_password)
    random.shuffle(random_password)
    random_password = ''.join(random_password)
    print(random_password, end='')



