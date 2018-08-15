#Loop used to check the user inputed valid units and if they want to do another conversion
needInput = 'yes'
while needInput == 'yes':
    #Prompts to recieve input
    enteredDistance = input('What is the distance?')
    enteredUnit = input('What are the input units?').lower()
    finalUnit = input('What are the output units?').lower()
    conversion = {'m': 1, 'ft': 0.3048, 'mi': 160934, 'km': 1000, 'yd': 0.9144, 'in': 0.0254, 'meters': 1,
                'feet': 0.3048, 'miles': 160934, 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}
    #Checks the enter valid units
    if enteredUnit not in conversion or finalUnit not in conversion:
        print('ERROR: You did not enter a valid input or output unit, try again.')
        continue
    else:
        #Converts the input to meters
        meterDistance = float(enteredDistance) * conversion[enteredUnit]
        #Converts from meters to output units
        finalDistance = format(meterDistance / float(conversion[finalUnit]), '.4g')
        print(f'{enteredDistance} {enteredUnit} is {finalDistance} {finalUnit}')
        needInput = input('Want to perform another unit conversion? (Type "yes" or "no")')