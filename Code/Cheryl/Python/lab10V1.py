#lab 10 version 1

nums = [5, 0, 8, 3, 4, 1, 6]
running = 0

for num in nums:
    print(running)
    running += num

# average = sum(nums) / len(nums)
average = running / len(nums)
print(f'The floor division average is: {average}')
