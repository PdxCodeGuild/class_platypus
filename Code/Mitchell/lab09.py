enteredDistance = input('What is the distance?')
enteredUnit = input('What are the units?').lower()
conversion = {'ft': 0.3048, 'mi': 160934, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
finalDistance = format(float(enteredDistance) * conversion[enteredUnit], '.4g')
print(f'{enteredDistance} {enteredUnit} is {finalDistance} m')