#lab 10 version 2 Average

nums = []
running = 0
answer = ''
user_nums = ''

while user_nums != 'done':
    try:
        user_nums = input('Please enter your number, or type \'done\' to get the average. >    ')
        user_nums = int(user_nums)
        user_nums = round(user_nums, 2)
        nums.append(user_nums)
        print(nums)

    except ValueError:
        for num in nums:
            running += num
            running = round(running, 2)
        print('Adding your numbers now...')
        average = running / len(nums)
        print(f'The average is: {average}')



