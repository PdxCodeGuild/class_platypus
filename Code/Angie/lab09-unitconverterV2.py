
units = {'ft': 0.3048, 'mi': 1609.34, 'km': 1000, 'm': 1, 'yd': 0.9144, 'in': 0.0254}

#y = 0.3048

while True:
    user = float(input('what is the distance?\n'))
    input_units = ''
    while input_units not in units:
        input_units = input(f'What are the units? ({", ".join(units.keys())})\n').lower()
    # if input_units == 'ft':
    #     value = user * 0.3048
    # elif input_units == 'mi':
    #     value = user * 1609.34
    # elif input_units == 'km':
    #     value = user * 1000
    # elif input_units =='m':
    #     value = user * 1

    value = user * units[input_units]

    print(f'{user} {input_units} is {value} m.')

    perform = input('Do you want to convert anything else?\n').lower()
    if perform == 'no':
        break
