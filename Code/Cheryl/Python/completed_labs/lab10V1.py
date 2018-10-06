#lab 10 version 1

nums = [5, 0, 8, 3, 4, 1, 6]
running = 0

for num in nums:
    running += num
    print(running)

average = running / len(nums)
print(f'The average is: {average}')
