# Numbers to Phrase
# By Skyler Parker
# Created on 16AUG18

# Imports

# Define global variables and lists

# Define Functions
def roman_numeral_conversion(input_number):
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    converted_number = ''

    if len(input_number) == 3:
        temp_input_number = input_number//100
        index_add = 2

    elif len(input_number) == 2:
        temp_input_number = input_number//10
        index_add = 1
    else:
        temp_input_number = input_number
        index_add = 0


user_number = int(input('Please enter a number between 1 and 1000 to be converted into Roman Numerals'))
        # print('The Roman Numeral equivalent is ', end='')
        # if 1000 <= user_number <= 3000:
        #     converted_number += roman_numerals[6]
        #
        # if 900 <= user_number <= 999:
        #     converted_number += roman_numerals[4] + roman_numerals[6]
        #
        # if 800 <= user_number <= 899:
        #     converted_number += roman_numerals[5] + roman_numerals[4]*3
        #
        # if 700 <= user_number <= 799:
        #     converted_number += roman_numerals[5] + roman_numerals[4]*2
        #
        # if 600 <= user_number <= 699:
        #     converted_number += roman_numerals[5] + roman_numerals[4]
        #
        # if 500 <= user_number <= 599:
        #     converted_number += roman_numerals[5]
        #
        # if 400 <= user_number <= 499:
        #     converted_number += roman_numerals[4] + roman_numerals[5]
        #
        # if 300 <= user_number <= 399:
        #     converted_number += roman_numerals[4]*3
        #
        # if 200 <= user_number <= 299:
        #     converted_number += roman_numerals[4]*2
        #
        # if 100 <= user_number <= 199:
        #     converted_number += roman_numerals[4]
        #
        # if 90 <= user_number <= 99 or 90 <= user_number % 100 <= 99:
        #     converted_number += roman_numerals[2] + roman_numerals[4]
        #
        # if 80 <= user_number <= 89 or 80 <= user_number % 100 <= 89:
        #     converted_number += roman_numerals[2] * 3
        #
        # if 70 <= user_number <= 79 or 70 <= user_number % 100 <= 79:
        #     converted_number += roman_numerals[2] * 2
        #
        # if 60 <= user_number <= 69 or 60 <= user_number % 100 <= 69:
        #     converted_number += roman_numerals[2]
        #
        # if 50 <= user_number <= 59 or 50 <= user_number % 100 <= 59:
        #     converted_number += roman_numerals[3]
        #
        # if 40 <= user_number <= 49 or 40 <= user_number % 100 <= 49:
        #     converted_number += roman_numerals[2] + roman_numerals[3]
        #
        # print(converted_number)

# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Convert Number to Phrase\n2 - Convert to Roman Numeral\n3 - Close Program'))

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
            print(tens)
            print('\n\nThe number you entered is spelled ' + ones_place[hundreds] + ' hundred and ', end='')

            if 20 <= user_number % 100 <= 99:
                print(tens_place[tens - 1] + '-' + ones_place[ones])

            elif 10 <= user_number % 100 <= 19:
                print(teens[user_number % 100 - 11])

            elif 0 <= user_number % 10 <= 10:
                print(ones_place[user_number % 10])




        else:
            print('The number must be 0 - 999; try again')






    elif menu_answer == 2:









    else:
        break