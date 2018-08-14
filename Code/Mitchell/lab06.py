import string
import random

#Ask the user for input
upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers = string.digits
specialCharacters = string.punctuation
numUpCase = input('Who many uppercase letters do you want your password to have?')
numLowCase = input('Who many lowercase letters do you want your password to have?')
numNums = input('Who many numbers do you want your password to have?')
numSpec = input('Who many uppercase letters do you want your password to have?')
#Randomly selects the need number of each type of character
current = 0
password = ''
while current < int(numUpCase):
 password = password + random.choice(upperCase)
 current = current + 1
current = 0
while current < int(numLowCase):
 password = password + random.choice(lowerCase)
 current = current + 1
current = 0
while current < int(numNums):
 password = password + random.choice(numbers)
 current = current + 1
current = 0
while current < int(numSpec):
 password = password + random.choice(specialCharacters)
 current = current + 1
#Randomizes the characters into the final password
current = 0
length = int(numUpCase) + int(numLowCase) + int(numNums) + int(numSpec)
while current < int(length):
 print(random.choice(password), end='')
 current = current + 1
