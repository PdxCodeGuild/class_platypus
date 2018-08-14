calculate = 'yes'
while calculate == 'yes':
    operation = input('Which opperation would you like to perform? (+, -, * or /)')
    firstNum = input('What is the first number?')
    secondNum = input('What is the second number?')
    if operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('ERROR: Please type the appropriate opperation sign you wish to perfom. (+, -, * or /)')
        continue
    elif operation == '+':
        sum = float(firstNum) + float(secondNum)
        print(firstNum + ' + ' + secondNum + ' = ' + str(sum))
    elif operation == '-':
        sum = float(firstNum) - float(secondNum)
        print(firstNum + ' - ' + secondNum + ' = ' + str(sum))
    elif operation == '*':
        sum = float(firstNum) * float(secondNum)
        print(firstNum + ' * ' + secondNum + ' = ' + str(sum))
    elif operation == '/':
        sum = float(firstNum) / float(secondNum)
        print(firstNum + ' / ' + secondNum + ' = ' + str(sum))
    calculate = input('Do you want to do another calculation? (Type "yes" or "no")')