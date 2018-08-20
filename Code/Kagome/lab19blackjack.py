print('Let\'s play Blackjack!')

def card_value(card):
    if card == 'A':
        return 1
    elif card == 'J' or 'K' or 'Q':
        return 10

def main():
    ans1 = input('Pick a card... ')
    ans2 = input('Pick a second card... ')
    ans3 = input('Pick a final card... ')

    total = card_value(ans1) + card_value(ans2) + card_value(ans3)

    if total < 17:
        print(f'{total} Hit!')
    elif total < 21:
        print(f'{total} Stay!')
    elif total == 21:
            print(f'{total} Blackjack!')
    else:
        print(f'{total} Busted!')
main()




