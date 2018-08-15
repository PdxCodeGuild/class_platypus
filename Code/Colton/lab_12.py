import random
while True:
    comp_num = random.randint(1, 10)
    while True:
        user_answer = input(f"Guess what number I am thinking?\n>")
        if user_answer == 'no':
            break
        user_answer =int(user_answer)
        if user_answer == comp_num:
            print("How\'d you know?")
            break
        elif user_answer != comp_num:
            print("NOPE!")
    if user_answer == 'no':
        break