cards = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

x = input('what is your first card? ').upper()
y = input('what is your second card? ').upper()
z = input('what is your third card? ').upper()

value = cards[x] + cards[y] + cards[z]

#print(value)

if value <= 17:
    print(f'{value} Hit!')

elif value == 21:
    print(f'Blackjack! you hit {value}!')

elif value > 21:
    print(f'{value} Bust!')

else:
    print(f'{value} Stay')







