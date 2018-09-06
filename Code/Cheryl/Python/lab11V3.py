
user_input = ''
while True:
    user_input = str.lower(input("Do you have a math problem? >   "))
    if user_input != 'yes':
        print("Thanks for looking. Have a great day!")
        break
    else:
        operation = input('Type in your math problem. >   ')
        print(eval(operation))





