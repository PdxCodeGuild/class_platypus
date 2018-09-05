deck_worth = {'A': 1, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

f_card = input(f"What's your first card? ")
f_card = deck_worth[f_card]
s_card = input(f"What's your second card? ")
s_card = deck_worth[s_card]


while True:
    if f_card + s_card < 17:
        print(f"{f_card + s_card} Hit")
        t_card = input(f"What's your third card? ")
        t_card = deck_worth[t_card]
        if f_card + s_card  + t_card < 17:
            print(f"{f_card + s_card + t_card} Hit")
            break
        elif f_card + s_card >= 17 and f_card + s_card < 21:
            print(f"{f_card + s_card + t_card} 'Stay'")
        elif f_card + s_card + t_card == 21:
            print("BLACKJACK!")
            break
        elif f_card + s_card + t_card > 21:
            print("BUSTED!")
            break
    elif f_card + s_card >= 17 and f_card + s_card < 21:
        print(f"{f_card + s_card} 'Stay'")
        break
    elif f_card + s_card == 21:
        print("BLACKJACK!")
        break