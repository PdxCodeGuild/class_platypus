"""
Lab 18: Peaks and Valleys
find 'peaks' and 'valleys' in a list of ints
a 'peak' is a number which is greater than the number on the left and right
a 'valley' is a number which is less that the number on the left and right

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
# >>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
# >>> peaks(data)
# [6, 14]
# >>> valleys(data)
# [9, 17]
"""


# find the indices of the peaks
def peaks(data):
    peak_indices = []
    for i in range(1, len(data)-1): #loop through the list, avoiding the end-points
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices


# find the indices of the valleys
def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley_indices.append(i)
    return valley_indices



'''
Here's an alternative version, using a regular for-loop with continue to over the first and last values.

def peaks(data):
    peak_indices = []
    for i in range(len(data)): #loop through the list, avoiding the end-points
        if i == 0 or i == len(data)-1:
            continue
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices
'''


def draw(data):
    largest = max(data)
    for i in range(largest, 0, -1):
        row = ''
        for j in range(len(data)):
            if i <= data[j]:
                row += 'X'
            else:
                row += ' '
        print(row)

# ;_;
# def let_it_rain_matthew_failure(data):
#     water = 0
#     for j in range(max(data), 0, -1):
#         row = ''
#         starting_index = 0
#         while starting_index < len(data):
#             while data[starting_index] < j and starting_index < len(data):
#                 starting_index += 1
#                 print(' ', end='')
#             print('X')
#
#         # while starting_index < len(data):
#         #     while data[starting_index] >= j:
#         #         starting_index += 1
#         #         if starting_index >= len(data):
#         #             break
#         #     ending_index = starting_index
#         #     while data[ending_index] < j:
#         #         ending_index += 1
#         #         if ending_index >= len(data):
#         #             break
#         #     water += ending_index - starting_index
#
#     print(water)


def draw_filled_maggie(data):  # uses a toggle to switch from space to fill
    graph = ''
    fill = False
    water = 0
    for line in range(max(data)):  # start with line 1, iterate through each line
        for i in range(len(data)):  # iterate through each space (x value) in the line
            if data[i] >= (max(data) - line):  # the first line should be the max, second line = max -1
                graph += ' x '
                fill = True
            else:
                if fill:
                    graph += ' 0 '
                    water += 1
                else:
                    graph += '   '
        if line != max(data) - 1:
            graph += '\n'  # skip a line at the end of each row, except for last line
        fill = False
    print(graph)
    print(data)
    print('amount of water collected: ', water, 'units')





def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9, 8, 7, 6, 5, 4]
    #print(peaks(data))
    #print(valleys(data))
    draw(data)
    print()
    print()
    print()
    draw_filled(data)

main()













