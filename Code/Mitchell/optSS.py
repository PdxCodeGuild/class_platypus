import random
sock_colors = ['Black', 'White', 'Blue']
sock_types = ['ankle', 'crew', 'calf', 'thigh']
socks = {}
# Generates 100 random sock colors and types then stores them in socks
for i in range(100):
    # Creates a random sock tuple with sock color and type
    random_sock = (sock_colors[random.randint(0, 2)], sock_types[random.randint(0, 3)])
    # If sock type is not in socks add it with value 1
    if random_sock not in socks:
        socks[random_sock] = 1
    # If sock type in dictionary increment the count
    else:
        socks[random_sock] += 1
# Loop through socks and calculate the number of pairs can be made for each key's value
for key, value in socks.items():
    # If the number of socks of a type is even no remainder
    if value % 2 == 0:
        print(f'{key[0]} {key[1]} socks can be divided into {int(value/2)} pairs with one remaining.')
    # If the number of socks of a type is odd account for remainder
    else:
        print(f'{key[0]} {key[1]} socks can be divided into {int((value-1)/2)} pairs with none remaining.')