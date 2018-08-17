# Lab 15 Version 2


user_input = int(input('Enter a number from 0-999.  >   '))
tens_digit = user_input//10
ones_digit = user_input%10
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
    if user_input < 20:
        if user_input in num_dict_teen:
            print(num_dict_teen[user_input])
        else:
            print(num_dict_ones[ones_digit])

def double_digit_num():
    if tens_digit in num_dict_tens and ones_digit in num_dict_ones:
        print(num_dict_tens[tens_digit], num_dict_ones[ones_digit])

if user_input < 100:
    zero()
    zero_ones_place()
    teens()
    double_digit_num()


#over 99
hundreds_digit = user_input//100
h_tens_digit = user_input%100 //10
h_ones_digit = user_input%10
num_dict_hundreds = {1: 'one hundred', 2: 'two hundred', 3: 'three hundred', 4: 'four hundred', 5: 'five hundred'}
h_num_dict_zero = {0: ''}
h_num_dict_ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
h_num_dict_teens = {11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
h_num_dict_second_digit ={1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

def h_zero_ones_place():
    if h_num_dict_zero:
        print('zero in the ones place is working')

def h_teens():
    if user_input > 110 and user_input < 120:
        if user_input in num_dict_teen:
            print(h_num_dict_teen[user_input])
        else:
            print(h_num_dict_ones[h_ones_digit])

def h_double_digit_num():
    if user_input > 119:
        if h_double_digit_num() in num_dict_hundreds and h_ones_digit in h_num_dict_ones:
            print('TEENS IS WORKING')
           # print(num_dict_hundreds[hundreds_digit], num_dict_tens[tens_digit], num_dict_ones[ones_digit])


def h_hundreds_digit_num():
    print('hundredds is working')

def hundreds_digit_num():
    if hundreds_digit in num_dict_hundreds and ones_digit in num_dict_ones:
        print(num_dict_hundreds[hundreds_digit], num_dict_tens[tens_digit], num_dict_ones[ones_digit])
if user_input > 99:
    h_zero_ones_place()
    h_teens()
    h_double_digit_num()
    h_hundreds_digit_num()



