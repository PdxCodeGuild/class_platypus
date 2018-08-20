#nums = []


def credit_validator():  # convert the input string into a list of ints
    credit = '4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'  # input('Please enter your credit card number for validation.')
    output = credit.split(' ')
    for i in range(len(output)):
        output[i] = int(output[i])

    check_digit = output.pop(-1)  # slice off the last digit
    output.reverse()  # reverse the digits

    for i in range(len(output)):
        if i % 2 == 0:  # Double every other element in the reversed list.
            output[i] *= 2

        if output[i] > 9:  # Subtract nine from numbers over nine
            output[i] -= 9

        sum()



    print(output)


credit_validator()



