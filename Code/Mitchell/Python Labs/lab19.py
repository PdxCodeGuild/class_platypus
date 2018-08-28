cardValue = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
firstCard = input('What\'s your first card? ').upper()
secondCard = input('What\'s your second card? ').upper()
thirdCard = input('What\'s your third card? ').upper()
cardTotal = cardValue[firstCard] + cardValue[secondCard] + cardValue[thirdCard]
action = ''
if cardTotal < 17:
    action = ' Hit'
elif cardTotal >= 17 and cardTotal < 21:
    action = ' Stay'
elif cardTotal > 21:
    action = ' Already Busted'
else:
    action = ' Blackjack!'
print(str(cardTotal) + action)