nums = []


def credit_validator():  # convert the input string into a list of ints
    credit = input('Please enter your credit card number for validation.')
    output = credit.split(' ')
    check_digit = output.pop(-1)  # slice off the last digit
    reversed(check_digit)  # reverse the digits

    print(output)


credit_validator()



