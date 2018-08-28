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
for sock in socks:
    if sock in sock_dict:
        sock_dict[key] += 1
    else:
        sock = sock_dict
print(sock_dict)