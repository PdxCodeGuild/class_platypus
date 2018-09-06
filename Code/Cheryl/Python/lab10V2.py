#lab 10 version 2

nums = []
running = 0
answer = ''
user_nums = ''

while answer != 'done':
    user_nums = int(input('Please enter your number >    '))
    nums.append(user_nums)
    print(nums)
    answer = input('If you are finished type done, or enter to continue.    ').lower()

print('Thanks for looking...')
for num in nums:
    print(running)
    running += num

# average = sum(nums) / len(nums)
average = running / len(nums)
print(f'The average is: {average}')



