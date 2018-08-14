calculate = 'yes'
while calculate == 'yes':
    operation = input('Which operation would you like to perform? (+, -, *, /, % or ^)').lower()
    firstNum = float(input('What is the first number?'))
    secondNum = float(input('What is the second number?'))
    #Addition operation
    if operation == '+' or operation == 'addition':
        sum = firstNum + secondNum
        print(f'{firstNum} + {secondNum} = {sum}')
    #Subtraction operation
    elif operation == '-' or operation == 'subtraction':
        difference = firstNum - secondNum
        print(f'{firstNum} - {secondNum} = {difference}')
    #Multiplication operation
    elif operation == '*' or operation == 'multiplication':
        product = firstNum * secondNum
        print(f'{firstNum} * {secondNum} = {product}')
    #Division operation
    elif operation == '/' or operation == 'division':
        quotient = firstNum / secondNum
        print(f'{firstNum} / {secondNum} = {quotient}')
    #Modulus operation
    elif operation == '%' or operation == 'mod':
        remainder = firstNum % secondNum
        print(f'{firstNum} % {secondNum} = {remainder}')
    #Power operation
    elif operation == '^' or operation == 'power':
        powerOf = float(firstNum)
        for i in range(1,int(secondNum)):
            powerOf = powerOf * float(firstNum)
        print(f'{firstNum} ^ {secondNum} = {powerOf}')
    calculate = input('Do you want to do another calculation? (Type "yes" or "no")')