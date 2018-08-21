# Credit Card Validation
# By Skyler Parker
# Created on 20AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Validate a Credit Card\n2 - Close Program'))

    if menu_answer == 1:
        card_number = input("Enter your credit card number: ")
        card_number = [int(x) for x in card_number]

        if len(card_number) == 16:

            check_digit = card_number[15]
            card_number = card_number[0:15]

            card_number.reverse()

            card_number = [x*2 for x in card_number]

            card_number = [x - 9 if x > 9 else x for x in card_number]

            card_number = sum(card_number)

            card_number %= 10

            if card_number == check_digit:
                print('This is a valid card number')

            else:
                print('This is not a valid card number')



    else:
        break