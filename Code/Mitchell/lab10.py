nums = []
sum = 0
inputValue = ''
#Recieves input from user to fill loop
while inputValue != 'done':
    inputValue = input('Enter a number, or "done": ').lower()
    if inputValue != 'done':
        nums.append(inputValue)
#Loop over the indices
for i in range(len(nums)):
        sum = sum + int(nums[i])
print('Average: ' + str(sum / len(nums)))