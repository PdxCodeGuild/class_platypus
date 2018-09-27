#lab 10 version 3

nums = []
running = 0
median = ''
user_nums = ''

while user_nums != 'done':
    try:
        user_nums = input('Please enter your number, or type \'done\' to get the median. >    ')
        user_nums = int(user_nums)
        user_nums = round(user_nums, 2)
        nums.append(user_nums)
        print(nums)

    except ValueError:

        nums.sort()
        length = len(nums)

        if len(nums) % 2 > 0:
            median_index = len(nums) // 2
            median = nums[median_index]
            print(f'The median number is: {median}')

        else:
            median_index = len(nums) // 2
            median = (nums[median_index] + nums[median_index - 1]) / 2
            print(f'The median number is: {median}')


