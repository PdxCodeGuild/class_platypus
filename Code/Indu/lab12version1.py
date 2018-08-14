#Guess the number
#created by Indu Thekkemeppilly Sivakumar on 08-14-2018
import random
i=0
while i<10:
 usernum = int(input("Guess a number between 0,10\n"))
 comp_num=random.randint(0,10)
 print (f"your number is {usernum} and computer's number is {comp_num}")
 count=0
 if usernum == comp_num:
     count = count+1
     print("you guessed correct")
 else :
     print ("Wrong!!")
 i=i+1
print(f"you guessed correct {count} times!")

