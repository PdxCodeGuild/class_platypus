tens = {0: '', 2: 'twenty-', 3: 'thirty-', 4: 'forty-', 5: 'fifty-', 6: 'sixty-', 7: 'seventy-', 8: 'eighty-',
        9: 'ninety-'}
ones = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
teens = {0: 'ten', 1: 'eleven', 2: 'twelve', 3: 'thirteen', 4: 'fourteen', 5: 'fifteen', 6: 'sixteen',
         7: 'seventeen', 8: 'eighteen', 9: 'nineteen'}
hundreds = {10: 'one-hundred', 11: 'one-hundred ten', 12: 'one-hundred twenty'}
while True:
    x = input("Enter number. ")
    if x == 'no':
        break
    x = int(x)
    if x >= 100 and x % 10 == 0:
        x = x // 10
        digit = x
        print(f"{hundreds[digit]}")
    if x >= 100 and x % 10 != 0:
        digit = x
        x = x // 10
        ones_digit = x % 10
        x = x % 10
        print(f"{hundreds[digit]} {ones[ones_digit]})")
    else:
        tens_digit = x // 10
        ones_digit = x % 10
        if x == 0:
            print('zero')
        elif tens_digit == 1:
            print(f"{teens[ones_digit]}")
        else:
            print(f"{tens[tens_digit]}{ones[ones_digit]}")
