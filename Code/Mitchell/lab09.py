#Prompts to recieve input
enteredDistance = input('What is the distance?')
enteredUnit = input('What are the input units?').lower()
finalUnit = input('What are the output units?').lower()
conversion = {'ft': 0.3048, 'mi': 160934, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
#Converts the input to meters
meterDistance = float(enteredDistance) * conversion[enteredUnit]
#Converts from meters to output units
finalDistance = format(meterDistance / float(conversion[finalUnit]), '.4g')
print(f'{enteredDistance} {enteredUnit} is {finalDistance} {finalUnit}')