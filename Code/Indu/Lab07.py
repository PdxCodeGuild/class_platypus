#rock paper scissors
import random
list = ['rock','paper','scissors']
player1  = input ("rock or paper or scissors\n")
player2 = random.choice(list)
print(f"player2 choose {player2}")
if player2 == player1:
   print("Tie! Try again")
elif player1 == 'rock' and player2 == 'paper':
       print("player 2 wins!")
elif player1 == 'rock' and player2 == 'scissors':
        print("Player 1 wins")
elif player1 == 'paper' and player2 == 'rock':
        print("Player 1 wins")
elif player1 == 'paper' and player2 == 'scissors':
        print(" player 2 wins")
elif player1 == 'scissors' and player2 == 'rock':
        print("Player 2 wins")
elif player1 == 'scissors' and player2 == 'paper':
        print(" player 1 wins")
