
while True:
    ops = input('What is the operation you\'d like to perform?')
    x = input('What is the first number?')
    y = input('What is the second number?')
    expression = x + ops + y
    value = eval(expression)
    print(value)
    perform = input('Do you want to compute anything else?').lower()
    if perform == 'no':
        break