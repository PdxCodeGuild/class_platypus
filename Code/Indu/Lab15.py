ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['zeroty', 'onety', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

num = int(input("Enter the number you want?\n"))
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
