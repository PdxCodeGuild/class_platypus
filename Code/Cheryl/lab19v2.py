# Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.

user_choice_one = input('Please choose one card:\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K, \nand I will give you advice on whether or not to\n \'Hit\', \'Stay\', or if you\'ve already \'Busted\' >   ').lower()

user_choice_two = input('Please choose another card:\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K >   ').lower()

user_choice_three = input('Please choose one card:\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K >   ').lower()

cards_info = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}

cards_ace =
if user_choice_one in cards_info and user_choice_two in cards_info and user_choice_three in cards_info:
    print('Your total points are: ', end=' ')
    cards_total = cards_info[user_choice_one] + cards_info[user_choice_two] + cards_info[user_choice_three]

if cards_total < 17:
    print('Hit!')

elif cards_total >= 17 and cards_total < 21:
    print('Stay')

elif cards_total == 21:
    print('Blackjack!')

else:
    print('You\'ve busted!')
