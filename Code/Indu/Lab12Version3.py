# Guess the number
# created by Indu Thekkemeppilly Sivakumar on 08-14-2018
import random

comp_num = random.randint(0, 10)
print(comp_num)
trial = 1
while True:
    usernum = int(input("Guess a number between 0,10\n"))
    # print (f"your number is {usernum} and computer's number is {comp_num}")
    if usernum == comp_num:
        print(f"you guessed correct in your {trial} try ")
        break
        # print (trial)
    else:
        if usernum > comp_num:
            print ("Wrong!! too high")
        else:
            print("Too low")

        trial = trial + 1
        repeat = input("Do you want to guess again? yes or no")
        if repeat == 'no':
            break
print("Good bye")

# print(f"you have tried {trial-1} times")
