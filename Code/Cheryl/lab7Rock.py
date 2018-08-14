
import random

print("Welcome to Rock, Paper, Scissors")

choices = ['rock', 'paper', 'scissors']
# outcomes_list = ['tie', 'win', 'lose']
user_choice = input(f"Choose {choices} >   ")
computer_choice = random.choice(choices)

print(f"You chose {user_choice} and the computer chose {computer_choice}. This means that:  ")

if user_choice == computer_choice:
    print("Tie")
elif user_choice == choices[0]:
    if computer_choice == choices[1]:
        print("You lose.")
    elif computer_choice == choices[2]:
        print("You win.")
elif user_choice == choices[1]:
    if computer_choice == choices[0]:
        print("You Win.")
    elif computer_choice == choices[2]:
        print("You lose.")
elif user_choice == choices[2]:
    if computer_choice == choices[1]:
        print("You Win.")
    elif computer_choice == choices[0]:
        print("You lose.")



