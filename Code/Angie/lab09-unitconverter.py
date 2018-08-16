
#units = {'mile': 1.0,'km': }

y = 0.3048

while True:
    user = float(input('what is the distance in feet?\n'))
    value = user * y
    print(f'{user} ft is {value} m.')

    perform = input('Do you want to convert anything else?\n').lower()
    if perform == 'no':
        break


