# Lab 15 Version 2 NEWER VERSION


user_input = input('Enter a number from 0-999.  >   ')
low_user_input = int(user_input)
tens_digit = low_user_input % 100 //10
ones_digit = low_user_input%10
i = 0


num_dict_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
num_dict_tens = {2:'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
num_dict_teen = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}

def zero():
    if tens_digit < 1 and ones_digit < 1:
        print('zero')

def zero_ones_place():
    if ones_digit == 0:
        print(num_dict_tens[tens_digit])

def teens():
    if low_user_input < 20:
        if low_user_input in num_dict_teen:
            print(num_dict_teen[low_user_input])
        else:
            print(num_dict_ones[ones_digit])

def double_digit_num():
    if tens_digit in num_dict_tens and ones_digit in num_dict_ones:
        print(num_dict_tens[tens_digit], num_dict_ones[ones_digit])

if low_user_input < 100:
    zero()
    zero_ones_place()
    teens()
    double_digit_num()

#over 99

# h_tens_digit = user_input%100 //10
# h_ones_digit = user_input%10
num_dict_hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred'}
h_num_dict_zero = {0: ''}
h_num_dict_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
h_num_dict_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
h_num_dict_second_digit = {2:'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}
h_num_dict_third_digit = {3: 'three hundred', 4: 'four hundred', 5: 'five hundred', 6: 'six hundred', 7: 'seven hundred', 8: 'eight hundred', 9: 'nine hundred'}


if low_user_input > 99:
    user_input_li = list(user_input)
    h_num_ones = int(user_input_li[2])
    h_num_tens = int(user_input_li[1])
    h_num_hundreds = int(user_input_li[0])
    hundreds_digit = low_user_input // 100

    # handling hundreds place
    print(h_num_dict_third_digit[hundreds_digit])

    # handling tens place
    if h_num_tens == 0:
        print('')
    else:
        print(h_num_dict_second_digit[tens_digit])

    #handling ones place
    if h_num_ones == 0:
        print(' ')
    else:
        print(h_num_dict_ones[ones_digit])




