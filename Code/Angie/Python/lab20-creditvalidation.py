def my_split(credit):
    return credit.split()


def str_int(list_of_stuff):
    for i in range(len(list_of_stuff)):
        list_of_stuff[i] = int(list_of_stuff[i])
    return list_of_stuff



def credit_validator(credit):  # convert the input string into a list of ints
      # input('Please enter your credit card number for validation.')
    output = my_split(credit)
    output = str_int(output)


    check_digit = output.pop(-1)  # slice off the last digit
    output.reverse()  # reverse the digits

    for i in range(len(output)):
        if i % 2 == 0:  # Double every other element in the reversed list.
            output[i] *= 2

        if output[i] > 9:  # Subtract nine from numbers over nine
            output[i] -= 9

    counter = 0
    for num in output:
        counter += num  # sum all values

    if counter % 10 == check_digit:
        print('this is a valid card')
        return True
    else:
        return False





print(credit_validator('4 5 5 6 7 3 7 5 8 6 8 9 9 8 5 5'))











