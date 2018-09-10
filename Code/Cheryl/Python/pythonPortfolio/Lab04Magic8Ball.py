import random

magic = ['Yes', 'No', 'The future is cloudy.', 'It has been decided in your favor.', 'You never know.', 'Try Again', 'Not Sure']
answer = 'yes'

print("Welcome to the Magic 8 Ball Game!")
while answer == 'yes':
    question = input("Ask the oracle your question: > ")
    print("The oracle says: " + random.choice(magic))
    answer = str.lower(input("Would you like to ask another question? Answer yes or no: > "))

print("Thanks for playing!")