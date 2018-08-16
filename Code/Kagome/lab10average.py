#nums = [5, 0, 8, 3, 4, 1, 6]


nums = []
while True:
    num_str = input("enter you numbers and 'done' when done ")
    if num_str == 'done':
        break
    else:
        nums.append(float(num_str))

total = 0
for num in nums:
    total += num
average = total/len(nums)
print(average)