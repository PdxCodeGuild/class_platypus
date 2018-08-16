data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
i = 1
peaks = []
valleys = []
peaksAndValleys = []
#Finds all peaks and valleys
for i in range(len(data) - 1):
    if data[i - 1] == data[i + 1]:
        #Finds all peaks
        if data[i] > data[i - 1] :
            peaks.append(i)
            peaksAndValleys.append(i)
        #Finds all valleys
        elif data[i] < data[i - 1] :
            valleys.append(i)
            peaksAndValleys.append(i)
#Prints peaks and valleys
peaksAndValleys.sort()
print(peaks)
print(valleys)
print(peaksAndValleys)
#Prints out chart with X's
row = [''] * 21
highest = max(data)
#Loops through rows
while highest > 0:
    #Loops through colums
    for i in range(len(data)):
        #print(valleys[0], highest)
        if data[i] >= highest:
            row[i] = 'X'
        else:
            row[i] = ' '
    highest = highest - 1
    print(''.join(row))
