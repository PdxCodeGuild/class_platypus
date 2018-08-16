data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
i = 1
peaks = []
valleys = []
peaksAndValleys = []
#Finds all peaks
for i in range(len(data) - 1):
    if data[i - 1] == data[i + 1]:
        if data[i] > data[i - 1] :
            peaks.append(i)
            peaksAndValleys.append(i)
#Finds all valleys
for i in range(len(data) - 1):
    if data[i - 1] == data[i + 1]:
        if data[i] < data[i - 1] :
            valleys.append(i)
            peaksAndValleys.append(i)
peaksAndValleys.sort()
print(peaks)
print(valleys)
print(peaksAndValleys)