card = {'A':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

first_card = input("What's your first card? \n")
second_card = input("What's your second card? \n")
third_card = input("What's your third card? \n")
#print(f"The first card is {first_card}and its value is {card[first_card]}'")
first_card = int(card[first_card])
second_card = int(card[second_card])
third_card = int(card[third_card])
sum = first_card+second_card+third_card
print(sum)
if  sum<17:
    print("Hit")
elif  sum < 21 and sum >= 17:
    print("Stay")
elif  sum == 21:
    print("Blackjack!!")
else:
    print("Busted")
