ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zero', '10ns', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#hundreds = ['one hundred','two hundred','three hundred','four hundred']

num = int(input("Enter the number you want to convert:\n"))
if num < 10:
    print(f"The number {num} is {ones[num]}")
elif num < 20:
    print(teens[num - 10])

elif num < 100:
    tens_digit = num // 10
    ones_digit = num % 10
    if ones_digit == 0:
        print(tens[tens_digit])
    else:
        print(tens[tens_digit] + '-' + ones[ones_digit])
elif num <1000:
    hundreds_digit = num // 100
    tens_digit = (num % 100)//10
    ones_num = (num%100)%10
    if tens_digit == 0 and ones_num ==0:
        print(f"{ones[hundreds_digit]} hundred")
    elif ones_num ==0:
        print(f"{ones[hundreds_digit]} hundred and {tens[tens_digit]}")
    else:
        print(f"{ones[hundreds_digit]} hundred and {tens[tens_digit]} {ones[ones_num]}")