# Numbers to Phrase
# By Skyler Parker
# Created on 16AUG18

# Imports

# Define global variables and lists

# Define Functions

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Convert Number to Phrase\n2 - Close Program'))

    if menu_answer == 1:

        ones_place = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
        tens_place = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        user_number = int(input('What number would like converted?'))

        if 0 <= user_number <= 10:
            print('\n\nThe number you entered is spelled ' + ones_place[user_number])

        elif 11 <= user_number <= 19:
            print('\n\nThe number you entered is spelled ' + teens[user_number - 11])

        elif 20 <= user_number <= 99:
            tens = user_number//10
            ones = user_number%10
            print(tens_place[tens - 1] + '-' + ones_place[ones])
        elif 100 <= user_number <= 999:
            hundreds = user_number//100
            tens = (user_number % 100)//10
            ones = user_number % 10

            print('\n\nThe number you entered is spelled ' + phrases)

        else:
            print('The number must be 0 - 999; try again')



    else:
        break