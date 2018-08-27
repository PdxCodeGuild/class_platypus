# Generate a list of 100 random socks, randomly chosen from a set of types:
import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']

socks = []
i = 0
while i < 100:
    i += 1
    output = random.choice(sock_types)
    socks.append(output)

sock_dict = {}

for key, val in socks:
    for key, val in to_add.items():
        if key in socks:
            sock[key] = [socks[key], val]
    else:
        sock_dict = sock
print(socks)
