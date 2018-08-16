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

        phrases = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'twenty',
                   'thirty',
                   'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety', 'one hundred', 'two hundred',
                   'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred', 'eight hundred',
                   'nine hundred']
        teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

        user_number = int(input('What number would like converted?'))

        if 0 <= user_number <= 10:
            print('\n\nThe number you entered is spelled ' + phrases[user_number])
        elif 11 <= user_number <= 19:
            print('\n\nThe number you entered is spelled ' + teens[user_number - 11])



    else:
        break