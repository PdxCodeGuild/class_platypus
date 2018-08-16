nums = [5, 0, 8, 3, 4, 1, 6]
sum = 0
#Loop over the indices
for i in range(len(nums)):
    sum = sum + int(nums[i])
print(sum / len(nums))