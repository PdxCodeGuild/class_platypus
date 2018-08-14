import random
Player_1 = ['rock', 'paper', 'scissors']
Player_2 = ['rock', 'paper', 'scissors']
while True:
    chosen_hand = input (f"What do you throw, {Player_1[0]}, {Player_1[1]}, or {Player_1[2]}?")
    comp_hand = random.choice(Player_2)
    if comp_hand == chosen_hand:
        print("Dang! It's a tie!")
    if comp_hand == 'rock':
        if chosen_hand == 'scissors':
            print("You lose! I chose rock!")
        elif chosen_hand == 'paper':
            print("You Beat me! I chose rock.")
    if comp_hand == 'paper':
        if chosen_hand == 'rock':
            print("You lose! I chose paper!")
        elif chosen_hand == 'scissors':
            print("You Beat me! I was paper.")
    if comp_hand == 'scissors':
        if chosen_hand == 'paper':
            print("You lose! I chose scissors!")
        elif chosen_hand == 'rock':
            print("You Beat me! I was scissors.")
    end_game = input (f"Want to play again yes or no? ")
    if end_game != 'yes':
        break


