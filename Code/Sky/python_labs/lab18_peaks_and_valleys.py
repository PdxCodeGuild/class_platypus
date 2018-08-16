# Peaks and Valleys
# By Skyler Parker and Colton Peterson
# Created on 16AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
peaks = []
valleys = []
peaks_and_valleys = []
max_value = 0
chart = []

for location in range(len(data) - 1):

    if data[location] > max_value:
        max_value = data[location]
    if location == 0:
        continue
    elif data[location] > data[location - 1] and data[location] > data[location + 1]:
        peaks.append(data[location])
        peaks_and_valleys.append(data[location])
    elif data[location] < data[location - 1] and data[location] < data[location + 1]:
        valleys.append(data[location])
        peaks_and_valleys.append(data[location])

for value in range(0, max_value):
    for location in range(len(data)):
        if data[location] >= max_value - value:
            print(' X ', end='')
        else:
            print('   ', end='')
    print('\n')










