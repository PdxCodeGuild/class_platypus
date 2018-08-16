

import random


# x = None
# if x is None:
#     print('x is none')
# if not x:
#     print('x is none')
# if x == None:
#     print('x is none')


comp_num = random.randint(1, 10)
guesses = []
while True:
    print(f'guessed so far: {guesses}')
    user_guess = int(input('what is your guess? '))
    if user_guess in guesses:
        print('you\'ve already guessed that')
    else:
        guesses.append(user_guess)

    if user_guess == comp_num:
        print(f'you won in {len(guesses)} guesses')
        break
    else:
        if user_guess < comp_num:
            print('too low!')
        else:
            print('too high!')

        if len(guesses) > 1:
            last_guess = guesses[len(guesses)-2]
            d1 = abs(comp_num-user_guess)
            d2 = abs(comp_num-last_guess)
            if d1 == d2:
                print('same distance!')
            elif d1 < d2:
                print('warmer!')
            else:
                print('colder!')



# comp_num = random.randint(1, 10)
# last_guess = None
# while True:
#     user_guess = int(input('what is your guess? '))
#     if user_guess == comp_num:
#         print('you won')
#         break
#     else:
#         if last_guess is not None:
#             if abs(comp_num-user_guess) < abs(comp_num-last_guess):
#                 print('warmer!')
#             else:
#                 print('colder!')
#     last_guess = user_guess


# input('pick a number, hit enter when ready...')
# for i in range(10):
#     correct = input(f'is it {i}?')
#     if correct == 'yes':
#         print('got it!')
#         break



# input('pick a number between 1 and 100, hit enter when ready...')
# lower = 1
# upper = 100
# while True:
#     # print(f'{lower} {upper}')
#     middle = (lower+upper)//2
#     correct = input(f'is it {middle}?')
#     if correct == 'yes':
#         print('got it!')
#         break
#     else:
#         direction = input('higher or lower?')
#         if direction == 'higher':
#             lower = middle
#         else:
#             upper = middle
#






