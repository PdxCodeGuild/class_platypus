# Lab 15 Version 1


user_input = int(input('Enter a number from 0-99.  >   '))


tens_digit = user_input//10
ones_digit = user_input%10
i = 0

num_dict_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
num_dict_tens = {2:'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
num_dict_teen = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

if tens_digit < 1 and ones_digit < 1:
        print('zero')

elif ones_digit == 0:
    print(num_dict_tens[tens_digit])
# else:

elif user_input < 20:
    if user_input in num_dict_teen:
        print(num_dict_teen[user_input])
    else:
        print(num_dict_ones[ones_digit])

elif tens_digit in num_dict_tens and ones_digit in num_dict_ones:
    print(num_dict_tens[tens_digit], end='-')
    print(num_dict_ones[ones_digit])




