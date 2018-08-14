calculate = 'yes'
while calculate == 'yes':
    operation = input('Which operation would you like to perform? (+, -, * or /)').lower()
    firstNum = float(input('What is the first number?'))
    secondNum = float(input('What is the second number?'))
    if operation == '+' or operation == 'addition':
        sum = firstNum + secondNum
        print(f'{firstNum} + {secondNum} = {sum}')

    elif operation == '-' or operation == 'subtraction':
        difference = firstNum - secondNum
        print(f'{firstNum} - {secondNum} = {difference}')

    elif operation == '*' or operation == 'multiplication':
        product = firstNum * secondNum
        print(f'{firstNum} * {secondNum} = {product}')

    elif operation == '/' or operation == 'division':
        quotient = firstNum / secondNum
        print(f'{firstNum} / {secondNum} = {quotient}')
    calculate = input('Do you want to do another calculation? (Type "yes" or "no")')