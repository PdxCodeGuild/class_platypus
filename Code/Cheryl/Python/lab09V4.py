#version 4 convert from any unit to any unit
welcome_mess = print('Welcome to the unit converter.')

meter_dist = 0
run_again = 'yes'

while run_again == 'yes':
    user_unit = str.lower(input('What unit would you like to convert FROM: ft, mi, m, yds, in, or km.  >   '))

    user_final_unit = str.lower(input('What unit would you like to convert TO: ft, mi, m, yds, in, or km.  >   '))

    user_dist = float(input(f'Please enter the distance you would like to convert from {user_unit}.  >   '))

#converts everything to meters
    if user_unit == 'km':
        meter_dist = user_dist * 1000

    elif user_unit == 'ft':
        meter_dist = user_dist * .3048

    elif user_unit == 'mi':
        meter_dist = user_dist * 1609.34

    elif user_unit == 'yds':
        meter_dist = user_dist * .9144

    elif user_unit == 'in':
        meter_dist = user_dist * 0.0254


#converts everything to whatever else they want
    if user_final_unit == 'in':
        meter_dist = meter_dist / 0.0254

    elif user_final_unit == 'yds':
        meter_dist = meter_dist / .9144

    elif user_final_unit == 'mi':
        meter_dist = meter_dist / 1609.34

    elif user_final_unit == 'km':
        meter_dist = meter_dist / 1000

    elif user_final_unit == 'ft':
        meter_dist = meter_dist / .3048

    elif user_final_unit == 'm':
        meter_dist = meter_dist

    meter_dist = round(meter_dist, 3)

    print(f"Your distance is: {meter_dist} {user_final_unit}.  ")
    run_again = str.lower(input("Would you like to run this again?  >  "))

print('Thanks for using the unit converter.')
