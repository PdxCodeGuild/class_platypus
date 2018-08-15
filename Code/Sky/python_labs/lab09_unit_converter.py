# Unit Converter
# By Skyler Parker
# Created on 15AUG18

# Imports

# Define global variables and lists
units = {"in": 0.0254, "ft": 0.3048, "yd": 0.9144, "m": 1, "mi": 1609.34, "km": 1000}


# Define Functions
def unit_converter(distance, starting_unit_type, converted_unit_type):
    return (distance*units[starting_unit_type])/units[converted_unit_type]


# Program Begins
while True:
    menu_answer = int(input('\nMenu:\n\n1 - Convert a new unit of measurement\n2 - Close Program'))

    if menu_answer == 1:
        print(f'What unit are you converting from? Your options are: ', end='')
        initial_unit = input(', '.join(units.keys()))
        initial_length = float(input('How long is the initial measurement?'))
        target_unit = input('What unit of measurement do you want to convert to?')

        if (initial_unit in units) and (target_unit in units):
            target_length = float(unit_converter(initial_length, initial_unit, target_unit))
            print(f"Your final measurement is {target_length}{target_unit}")
        else:
            print('You unit type selections are not valid >.<')
    else:
        break

