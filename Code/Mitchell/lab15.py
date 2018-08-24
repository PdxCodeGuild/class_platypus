# Dictionaries with words for each number
tensDigits = {2: 'twenty', 3: 'thir', 4: 'four', 5: 'fif', 6: 'six', 7: 'seven', 8: 'eigh', 9: 'nine'}
onesDigits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
action = input('Do you want to change a number to phrase or a time to phrase? (Type "number or "time"): ').lower()
#Changes entered number digits to a phrase.
if action == 'number':
    num = int(input('Enter a number between 0 and 9,999: '))
    #Cases for four digit numbers
    thousands_digit = num//1000
    if thousands_digit > 0:
        print(onesDigits[thousands_digit] + ' thousand ', end='')
        num = num - (1000 * thousands_digit)
    #Cases for three digit numbers
    hundreds_digit = num//100
    if hundreds_digit > 0:
        print(onesDigits[hundreds_digit] + ' hundred ', end='')
        num = num - (100 * hundreds_digit)
    #Define tens_digit after removing hundreds and thousands
    tens_digit = num//10
    ones_digit = num%10
    #Cases for multiples of one hundred
    if tens_digit == 0 and ones_digit == 0:
        exit()
    #Cases for single digit
    if tens_digit == 0 or tens_digit == '':
        print(onesDigits[ones_digit])
    #Cases for ten through teens
    elif tens_digit == 1:
        if ones_digit > 2 and ones_digit != 5:
            print(tensDigits[ones_digit] + 'teen')
        elif ones_digit == 0:
            print('ten')
        elif ones_digit == 1:
            print('eleven')
        else:
            print('twelve')
    #Cases for multiples of ten
    elif ones_digit == 0:
        print(tensDigits[tens_digit] + 'ty')
    else:
        print(tensDigits[tens_digit] + 'ty-' + onesDigits[ones_digit])
#Changes entered time into a phrase
elif action == 'time':
    time = input('Enter a time in digits with a ":" dividing the hour and minute digits: ')
    colon = time.index(':')