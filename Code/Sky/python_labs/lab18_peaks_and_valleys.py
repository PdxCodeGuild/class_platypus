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
water_total = 0

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

    chart_row = []

    for location in range(len(data)):
        if data[location] >= max_value - value:
            chart_row.append('X')
        else:
            chart_row.append('Z')
    chart.append(chart_row)





for row in chart:

    water_toggle = False
    water_temp_total = 0
    water_start = 0
    water_end = 0
    land_toggle = False

    water_temp_total = 0

    for value in range(len(row)):

        if row[value] == 'X' and not land_toggle and not water_toggle:
            land_toggle = True

        elif land_toggle and row[value] == 'Z':
            water_toggle = True
            water_temp_total += 1
            water_start = value
            land_toggle = False

        elif land_toggle and row[value] == 'X':
            pass

        elif water_toggle and row[value] == 'Z':
            water_temp_total += 1
            water_end = value

        elif water_toggle and row[value] == 'X':
            water_toggle = False
            land_toggle = True
            water_total += water_temp_total

        elif water_toggle and row[value] == 'Z' and water_start == 0:
            print('test')
            water_temp_total += 1

            water_start = value

        elif water_toggle and row[value] == 'X':
            water_toggle = False
            water_end = value-1
            water_total += water_temp_total

        for location in range(water_start, water_end):
            row[value] = 'O'
        print(water_toggle)
        print(water_start)

print(water_total)

for row in chart:
    for value in row:
        if value == 'X':
            print(' X ', end='')
        elif value == 'O':
            print(' O ', end='')
        else:
            print('   ', end='')
    print('\n')

# for value in range(0, max_value):
#
#
#     for location in range(len(data)):
#         print(data[location])
#         if data[location] == 'X':
#             water_toggle = True
#             print('test')
#         elif water_toggle is True and data[location] == 'Z':
#             water_temp_total += 1
#             print('test')
#         elif water_toggle is True and data[location] == 'X':
#             water_toggle = False
#             water_total += water_temp_total
#
#     water_toggle = False
#     water_temp_total = 0









