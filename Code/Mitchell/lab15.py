# Dictionaries with words for each number
tensDigits = {2: 'twenty', 3: 'thir', 4: 'four', 5: 'fif', 6: 'six', 7: 'seven', 8: 'eigh', 9: 'nine'}
onesDigits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
x = 90
tens_digit = x//10
ones_digit = x%10
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