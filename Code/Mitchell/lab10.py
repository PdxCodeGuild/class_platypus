nums = []
sum = 0
inputValue = ''
#Recieves input from user to fill loop
while inputValue != 'done':
    inputValue = input('Enter a number, or "done": ').lower()
    if inputValue != 'done':
        nums.append(int(inputValue))
#Loop over the indices
for i in range(len(nums)):
        sum = sum + nums[i]
nums.sort()
#Calculate average
print('Average: ' + str(sum / len(nums)))
#Calculate median
if len(nums) % 2 == 1:
    median = nums[int((len(nums) - 1) / 2)]
else:
    median = (nums[int(len(nums) / 2)] + nums[int(len(nums) / 2 - 1)]) / 2
print('Median: ' + str(median))