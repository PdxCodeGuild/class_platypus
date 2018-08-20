#lab 20 version 1

user_card_nums = input('What are the digits of your credit card? >  ')
user_card_nums = list(user_card_nums)

user_card_nums = [int(x) for x in user_card_nums] #converts to an int

#pop off last num
check_digit = user_card_nums.pop()

#reverse
user_card_nums.reverse()

#double every other element
odd_nums = user_card_nums[1::2] #odd numbers
double_nums = [x * 2 for x in odd_nums]
print(f'{double_nums} + I\'m double')

#subtract nine from numbers over 9
i = 0
while i < len(double_nums):
    if double_nums[i] > 9:
         print(f'{double_nums} {double_nums[i] - 9} I am subtract 9')
    i += 1

# print(user_card_nums)
