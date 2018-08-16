#version 2

welcome_mess = print('Welcome to the meter converter.')

new_dist = 0
run_again = 'yes'

while run_again == 'yes':
    user_unit = str.lower(input('Please name the unit type you would like to convert: ft, mi, m, or km.  >   '))
    user_dist = float(input(f'Please enter the distance you would like to convert to meters from {user_unit}.  >   '))

    if user_unit == 'km':
        new_dist = user_dist * 1000

    elif user_unit == 'ft':
        new_dist = user_dist * .3048

    elif user_unit == 'mi':
        new_dist = user_dist * 1609.34

    elif user_unit == 'm':
        new_dist = user_dist

    print(f"Your distance is: {new_dist} meters.  ")
    run_again = str.lower(input("Would you like to run this again?  >  "))

print('Thanks for using the meter converter.')


