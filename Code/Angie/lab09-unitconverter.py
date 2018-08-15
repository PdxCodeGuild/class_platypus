
#units = {'mile': 1.0,'km': }

y = 0.3048

while True:
    user = int(input('what is the distance in feet?'))
    expression = user * float(y)
    value = eval('expression')
    print(f'{user} ft is {value} m.')

    perform = input('Do you want to convert anything else?').lower()
    if perform == 'no':
        break


