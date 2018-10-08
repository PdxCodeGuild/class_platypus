
welcome_mess = print(f'\nWelcome to the Calculator.\n ')
calc = 'yes'

while calc == 'yes':
    operation = input('What operation would you like to perform? (Type \'done\' to exit the program.) *, -, +, or / >   ')
    if operation == 'done':
        print("Have a nice day!")
        break

    first_number = float(input("What is your first number? >   "))
    second_number = float(input("What is your second number? >   "))


    print(first_number, operation, second_number, ' = ')
    if operation == '*':
        print(first_number * second_number)
    elif operation == '+':
        print(first_number + second_number)
    elif operation == '-':
        print(first_number - second_number)
    elif operation == '/':
        print(first_number / second_number)



