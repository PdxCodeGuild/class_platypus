# Average Number
# By Skyler Parker
# Created on 16AUG18

# Imports
import random
# Define global variables and lists

# Define Functions


def averages(nums):
    total = float(0)
    num_count = 0
    for num in nums:
        total += float(num)
        num_count += 1
    average = total / num_count
    print('The average of the numbers you enter is: ' + str(average))


def median(nums):
    total = float(0)
    nums.sort()
    print(nums)


# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Find an average number\n2 - Close Program'))

    if menu_answer == 1:
        numbers = []
        while True:
            num = input('Enter a number, or "done": ')
            if num == 'done':
                break
            else:
                numbers.append(num)
        if len(numbers) == 0:
            print('\n\nYou entered no numbers, would you like to try again?')
        else:
            print('\n')
            print(numbers)
            # averages(numbers)
            median(numbers)

    else:
        break

