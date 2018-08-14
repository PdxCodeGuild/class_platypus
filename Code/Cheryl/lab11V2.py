#
# Allow the user to keep performing operations until they say 'done'. Use while True and break. Below is some sample input/output.
#
# > what is the operation you'd like to perform? +
# > what is the first number? 5
# > what is the second number? 12
# > 5 + 12 = 17
# > what is the operation you'd like to perform? done
# > goodbye!



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
