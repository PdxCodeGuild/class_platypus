while True:
    x = (input("Enter number. "))
    if x == 'no':
        break
    if int(x) // 10 >= 10:
        x = int(x) // 10
        digit = int(x)
        hundreds = {10: 'one-hundred'}
        print(f"{hundreds[digit]}")
    else:
        x = int(x)
        tens_digit = x // 10
        ones_digit = x % 10
        if x == 0:
            print('zero')
        elif tens_digit == 1:
            teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen', 7: 'seventeen', 8: 'eighteen', 9:'nineteen'}
            print(f"{teens[ones_digit]}")
        else:
            tens = {0: '', 2: 'twenty-', 3: 'thirty-', 4: 'forty-', 5: 'fifty-', 6: 'sixty-', 7: 'seventy-', 8: 'eighty-', 9: 'ninety-'}
            ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
            print(f"{tens[tens_digit]}{ones[ones_digit]}")
