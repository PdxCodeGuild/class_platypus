# Average Number
# By Skyler Parker
# Created on 16AUG18

# Imports
import random
import math
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
    if len(nums) % 2 == 1:
        median_loc = math.ceil(len(nums)/2 - 1)
        print('The median numbers are: ' + nums[median_loc])
    else:
        medians = []
        median_loc = int(len(nums)/2)
        medians.append(nums[median_loc - 1])
        medians.append(nums[median_loc])
        print('The median numbers are: ' + str(medians[0]) + ' and ' + str(medians[1]))


def mode(nums):
    number_count = {}
    for number in nums:
        if number in number_count:
            print(number_count[number])
            number_count[number] = number_count[number] + 1
        else:
            number_count[number] = 1

    mode_numbers = {}
    median_amount = 0
    for number in number_count:
        if number_count[number] > median_amount:
            median_amount = number_count[number]

    print median amount



    print('----')
    print(number_count)



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
            # averages(numbers)
            # median(numbers)
            mode(numbers)

    else:
        break

