import random
sock_types = ['ankle', 'crew', 'calf', 'thigh']
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
print(socks)