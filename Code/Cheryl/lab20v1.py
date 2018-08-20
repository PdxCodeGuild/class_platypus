#lab 20 version 1

user_card_nums = input('What are the digits of your credit card? >  ').split()

list(user_card_nums)

user_card_nums.pop(-1)

print(user_card_nums)