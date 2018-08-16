#nums = [5, 0, 8, 3, 4, 1, 6]


nums = []
while True:
    num_str = input("enter your numbers and 'done' when done... ")
    if num_str == 'done':
        break
    else:
        nums.append(float(num_str))

def mean(nums):
    # total = 0
    # for num in nums:
    #     total += num
    # average = total/len(nums)
    # return average

    average =sum(nums)/len(nums)
    return average

print(mean(nums))

def median(nums):
    nums = nums.copy()
    nums.sort()
    if len(nums)%2 == 0:
        a = nums[len(nums)//2-1]
        b = nums[len(nums)//2]
        return [a,b]
    else:
        return [nums[len(nums)//2]]

# def mode(nums):
#     counts = {}
#     for num in nums:
#         if num in counts:
#             counts[num] += 1
#         else:
#             counts[num] = 1
#         print(f'{num} {counts})





