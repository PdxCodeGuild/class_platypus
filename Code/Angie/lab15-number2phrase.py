
digit = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

x = 99

tens_digit = x // 10
ones_digit = x % 10



# print(tens_digit, ones_digit)

if x <= 19:
    print(digit[x])

else:
    print(tens[tens_digit], digit[ones_digit])




#Hint 2: use the digit as an index for a list of strings