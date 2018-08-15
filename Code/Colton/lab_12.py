# import random
# while True:
#     comp_num = random.randint(1, 10)
#     while True:
#         user_answer = input(f"Guess what number I am thinking?\n>")
#         if user_answer == 'no':
#             break
#         user_answer =int(user_answer)
#         if user_answer == comp_num:
#             print("How\'d you know?")
#             break
#         elif user_answer != comp_num:
#             print("NOPE!")
#     if user_answer == 'no':
#         break





# import random
# while True:
#     comp_num = random.randint(1, 10)
#     while True:
#         user_answer = input(f"Guess what number I am thinking?\n>")
#         if user_answer == 'no':
#             break
#         user_answer = int(user_answer)
#         if user_answer < comp_num:
#             print("Too low!")
#         elif user_answer > comp_num:
#             print("Too high!")
#         if user_answer == comp_num:
#             print("How\'d you know?")
#             break
#     if user_answer == 'no':
#         break

import random

while True:
    comp_num = random.randint(1, 10)
    last_answer = None
    while True:
        answer = input(f"Guess what number I am thinking between 1 and 10?\n>")
        if answer == 'no':
            break
        answer = int(answer)
        if (answer) == comp_num:
            print("How\'d you know?")
        else:
            if last_answer is not None:
                if abs(last_answer - comp_num) < abs(answer - comp_num):
                    print("further")
                else:
                    print("closer")
        answer = last_answer