# Numbers to Phrase
# By Skyler Parker
# Created on 16AUG18

# Imports

# Define global variables and lists

# Define Functions


def roman_numeral_conversion(input_number):
    roman_numerals = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    converted_number = ''

    if len(str(input_number)) == 4:
        temp_input_number = input_number//1000
        next_number = input_number % 1000
        index_add = 6

    elif len(str(input_number)) == 3:
        temp_input_number = input_number//100
        next_number = input_number % 100
        index_add = 4

    elif len(str(input_number)) == 2:
        temp_input_number = input_number//10
        next_number = input_number % 10
        index_add = 2
    else:
        temp_input_number = input_number
        index_add = 0

    if temp_input_number == 9:
        converted_number += roman_numerals[0 + index_add] + roman_numerals[2 + index_add]

    elif temp_input_number == 8:
        converted_number += roman_numerals[1 + index_add] + roman_numerals[0 + index_add]*3

    elif temp_input_number == 7:
        converted_number += roman_numerals[1 + index_add] + roman_numerals[0 + index_add]*2

    elif temp_input_number == 6:
        converted_number += roman_numerals[1 + index_add] + roman_numerals[0 + index_add]

    elif temp_input_number == 5:
        converted_number += roman_numerals[1 + index_add]

    elif temp_input_number == 4:
        converted_number += roman_numerals[0 + index_add] + roman_numerals[1 + index_add]

    elif temp_input_number == 3:
        converted_number += roman_numerals[0 + index_add]*3

    elif temp_input_number == 2:
        converted_number += roman_numerals[0 + index_add]*2

    elif temp_input_number == 1:
        converted_number += roman_numerals[0 + index_add]

    if len(str(input_number)) > 1:
        converted_number += roman_numeral_conversion(next_number)
    return converted_number


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
        user_number = int(input('What number, between 1 and 3999, would like converted?'))
        print('The number you enter is written in roman numerals like this: ', end='')
        print(roman_numeral_conversion(user_number))









    else:
        break