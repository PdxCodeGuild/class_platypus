
user_input = 'yes'
while True:

    if user_input != 'yes':
        print("Thanks for looking. Have a great day!")
        break
    else:
        operation = input('Type in your math problem. >   ')
        print(f'{operation} = {eval(operation)}')

    user_input = str.lower(input("Do you have another math problem? >   "))




