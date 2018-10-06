

calc = 'yes'

while calc == 'yes':
    operation = input('What operation would you like to perform? *, -, +, or / >   ')
    first_number = float(input("What is your first number? >   "))
    second_number = float(input("What is your second number? >   "))


    print(first_number, operation, second_number, ' = ')
    if operation is '*':
        print(first_number * second_number)
    elif operation is '+':
        print(first_number + second_number)
    elif operation is '-':
        print(first_number - second_number)
    elif operation is '/':
        print(first_number / second_number)

    calc = str.lower(input("Would you like to perform another calculation? Answer yes or no: > "))
