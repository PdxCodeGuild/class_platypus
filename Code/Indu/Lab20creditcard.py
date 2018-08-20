# credit card validation
# created by Indu Thekkemeppilly Sivakumar on 08/20/2018
card_num = input("please enter your creditcard number: \n")
# Check if the number entered has 16 digits)
if len(card_num) != 16:
    print("invalid")
else:
    print("Thanks")
card = []
for i in range(len(card_num)):
    card.append(int(card_num[i]))
# print (card)
# Check digit is the last digit of the credit card number
check_digit = card.pop(-1)
# print(check_digit,card)
card.reverse()
# print(card)
for i in range(0, len(card), 2):
    card[i] *= 2
print(card)
# Subtract nine from numbers over nine
sum_digit = 0
for i in range(len(card)):
    if card[i] > 9:
        card[i] -= 9
    sum_digit = sum_digit + card[i]
print(sum_digit)
# find if check digit and last digit of sum are equal
if sum_digit % 10 == check_digit:
    print("card is valid!")
else:
    print("invalid card")
