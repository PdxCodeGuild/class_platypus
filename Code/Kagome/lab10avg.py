#nums = [5, 0, 8, 3, 4, 1, 6]


nums = []
while True:
    num_str = input("enter your numbers and 'done' when done... ")
    if num_str == 'done':
        break
    else:
        nums.append(float(num_str))

def mean(nums):
    total = 0
    for num in nums:
        total += num
    average = total/len(nums)
    return average

print(mean(nums))

