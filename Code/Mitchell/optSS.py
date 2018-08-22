import random
sock_types = ['Ankle', 'Crew', 'Calf', 'Thigh']
socks = {}
# Generates 100 random sock types and stores them in socks
for i in range(100):
    random_sock = sock_types[random.randint(0, 3)]
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
        print(f'{key} socks can be divided into {int(value/2)} pairs with one remaining.')
    # If the number of socks of a type is odd account for remainder
    else:
        print(f'{key} socks can be divided into {int((value-1)/2)} pairs with none remaining.')