
digit = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundreds = ['', 'hundred']

x = 100



#print(hundred_digit)
#print(tens_digit)

if x <= 19:
    print(digit[x])
elif x < 100:
    tens_digit = x // 10
    ones_digit = x % 10
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        print(tens[tens_digit] + '-' + digit[ones_digit])
elif x < 1000:
    ones_digit = x % 10
    tens_digit = x // 10
    hundred_digit = (x // 100) % 10
    print(digit[ones_digit] + ' ' + hundreds[hundred_digit] + ' ' + tens[tens_digit] + ' ' + digit[ones_digit])




#Hint 2: use the digit as an index for a list of strings