#lab 10 version 3

nums = []
# running = 0
answer = ''
user_nums = ''
median = 0
median_index = 0

while answer != 'done':
    user_nums = int(input('Please enter your number >    '))
    nums.append(user_nums)
    print(nums)
    answer = input('If you are finished type done, or enter to continue.    ').lower()

print('Calculating...')


# median number you need to sort first, then pick the center number by getting the average of the list
nums.sort()
length = len(nums)

if len(nums) % 2 > 0:
    median_index = len(nums) // 2
    median = nums[median_index]
    print(median)

# else:
#     median_index = len(nums) // 2
#     median_index_2 = median_index + 1
#     median = (nums[median_index] + nums[median_index_2]) // 2

    print(nums[median])

# median = length / 2
# round(median, 1)
# print(f'The median is: {median}')
