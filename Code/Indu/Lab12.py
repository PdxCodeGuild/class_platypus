#Guess the number
#created by Indu Thekkemeppilly Sivakumar on 08-14-2018
import random
comp_num = random.randint(0, 10)
print(comp_num)
while True:
 usernum = int(input("Guess a number between 0,10\n"))
 trial =1
# print (f"your number is {usernum} and computer's number is {comp_num}")
 if usernum == comp_num:
     print(f"you guessed correct in your {trial} try ")
     #print (trial)
 else :
     print ("Wrong!!")
     trial= trial+1
 repeat = input("Do you want to guess again? yes or no")
 if repeat == 'no':
     break
print("Good bye")

#print(f"you have tried {trial-1} times")
