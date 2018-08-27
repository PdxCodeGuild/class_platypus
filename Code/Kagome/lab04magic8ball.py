import random

answers = input('Ask Me Any Question\n:')
eight_ball = [ "Yes! Always!", "It Is So", "Without A Doubt", "Yes, Definitely",
               "No", "Never", "Don't Count On It", ]
print(random.choice(eight_ball))

while True:
    input('Ask Another Question...')
    print(random.choice(eight_ball))
    if input('Type yes to continue...') != 'yes':
        break


