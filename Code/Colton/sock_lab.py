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
    if key in socks:
            [key] = [sock_dict[key], val]
print(sock_dict)
