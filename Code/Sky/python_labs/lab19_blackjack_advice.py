# BlackJack Advice
# By Skyler Parker
# Created on 20AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Play a Hand\n2 - Close Program'))

    if menu_answer == 1:
        card_values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                       '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
        first_card = card_values[input('What\'s your first card?')]
        second_card = card_values[input('What\'s your second card?')]
        third_card = card_values[input('What\'s your second card?')]

        total = first_card + second_card + third_card

        if first_card == 1 and total <= 11:
            total += 10
        if second_card == 1 and total <= 11:
            total += 10
        if third_card == 1 and total <= 11:
            total += 10

        print('\nYour current hand is worth: ' + str(total))
        if total > 21:
            print('You are already busted!')
        elif total == 21:
            print('Blackjack!')
        elif total >= 17:
            print('Stay!')
        else:
            print('Hit')

    else:
        break