# Lab: Sock Sorter
# You've just finished laundry and your expansive sock collection is in complete disorder. Sort your socks into pairs and pull out any loners.
#
# Generate a list of 100 random socks, randomly chosen from a set of types: sock_types = ['ankle', 'crew', 'calf', 'thigh']
#
# Find the number of duplicates and loners for each sock type. Hint: dictionaries are helpful here.


import random

sock_types = ['ankle', 'crew', 'calf', 'thigh']


eye = 0
while eye < 100:
    sock_types.append(random.choice(sock_types))
    eye += 1

ankle_list = []
i = 0
ankle_count = 0
crew_count = 0
for i in sock_types:
    if 'ankle' in sock_types:
        ankle_count += 1
    if 'crew' in sock_types:
        crew_count += 1
print(f'There are {ankle_count} ankle socks in your box.')
print(f'There are {crew_count} crew socks in your box. ')

