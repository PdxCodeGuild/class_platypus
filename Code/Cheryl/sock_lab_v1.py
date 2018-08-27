# Lab: Sock Sorter
# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.
#
# Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']
#
# Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.


import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']


print(type(sock_types))

eye = 0
while eye < 100:
    sock_types.append(random.choice(sock_types))
    eye += 1


print(sock_types)