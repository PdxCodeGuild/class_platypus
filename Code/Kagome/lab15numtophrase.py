
# dict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four', 5 : 'five',
#           6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine', 10 : 'ten',
#           11 : 'eleven', 12 : 'twelve', 13 : 'thirteen', 14 : 'fourteen',
#           15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen', 18 : 'eighteen',
#           19 : 'nineteen', 20 : 'twenty',
#           30 : 'thirty', 40 : 'forty', 50 : 'fifty', 60 : 'sixty',
#           70 : 'seventy', 80 : 'eighty', 90 : 'ninety' }



ones = ['and zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['and zero', 'one', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def get_tens_phrase(num):
    if num < 10:
        return ones[num]
    elif num < 20:
        return teens[num - 10]
    elif num < 100:
        tens_digit = num // 10
        ones_digit = num % 10
        if ones_digit == 0:
            return tens[tens_digit]
        else:
            return tens[tens_digit] + ''+ ones[ones_digit]

def get_hundreds_phrase(num):
    tens_num = num % 100
    hundreds_digit = num // 100

    hundreds_phrase = ones[hundreds_digit]+' hundred'

    return hundreds_phrase + ' ' + get_tens_phrase(tens_num)


def get_thousands_phrase(num):
    hundreds_num = num % 1000
    thousands_digit = num // 1000

    thousands_phrase = tens[thousands_digit]+' thousand'

    return thousands_phrase + '' + get_hundreds_phrase(hundreds_num)



num = int(input('what is your number? '))

if num < 10:
    print(get_ones_phrase(num))
elif num < 100:
    print(get_tens_phrase(num))
elif num < 1000:
    print(get_hundreds_phrase(num))
elif num < 10000:
    print(get_thousands_phrase(num))



