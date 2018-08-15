#Guess the number
#created by Indu Thekkemeppilly Sivakumar on 08-14-2018
import random
i=0
print("You have a maximum of 10 guesses")
comp_num=random.randint(0,10)
while i<10:
 print(f"you have {10-i}trials left")
 usernum = int(input("Guess a number between 0,10\n"))
 print(comp_num)
 if usernum == comp_num:
     print(f"you guessed correct in your {i+1}th try")
     print(f"the number chosen by computer was {comp_num}")
     break
 else :
     print ("Wrong!! Try again!")
 i=i+1
