
import random

print("Welcome to Rock, Paper, Scissors")

choices = ['rock', 'paper', 'scissors']
play = True
i = 1

while i >= 1:
    user_choice = input(f"Choose {choices} >   ")
    computer_choice = random.choice(choices)
    print(f"You chose {user_choice} and the computer chose {computer_choice}. This means that:  ")
    if user_choice == computer_choice:
        print("You have a tie")
    elif user_choice == choices[0]:
        if computer_choice == choices[1]:
            print("You Lose")
        elif computer_choice == choices[2]:
            print("You Win!")
    elif user_choice == choices[1]:
        if computer_choice == choices[0]:
            print("You Win!")
        elif computer_choice == choices[2]:
            print("You Lose")
    elif user_choice == choices[2]:
        if computer_choice == choices[1]:
            print("You Win!")
        elif computer_choice == choices[0]:
            print("You Lose")


        if user_choice == computer_choice:
            print('You have a tie')
            break
        elif user_choice == choices[0]:
            if computer_choice == choices[1]:
                print('You Lose')
                break
            else:
                print("You Win!")
                break
    play = input('Would you like to play again? >  ').upper()
    if play == 'YES':
        i + 1
    else:
        i = 0
        print('Thanks for playing!')
        break