
welcome_mess = print('Welcome to the unit converter.')

meter_dist = 0
run_again = 'yes'

user_unit = 0
out_dist = 0

while run_again == 'yes':

    user_unit = str.lower(input('What unit would you like to convert FROM: ft, mi, m, yds, in, or km.  >   '))

    user_final_unit = str.lower(input('What unit would you like to convert TO: ft, mi, m, yds, in, or km.  >   '))

    while True:
        try:
            user_dist = float(input(f'Please enter the distance you would like to convert from {user_unit}.  >   '))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


    user_dist = round(user_dist, 3)

    to_meter_dictionary = {'km': user_dist * 1000, 'm': user_dist, 'ft': user_dist * .3048, 'in': user_dist * 0.0254, 'yds': user_dist * .9144, 'mi': user_dist * 1609.34}
    from_meter_dictionary = {'km': 1000, 'm': 1, 'in': 0.0254, 'ft': .3048, 'yds': .9144, 'mi': 1609.34}

    if user_unit in to_meter_dictionary and user_final_unit in from_meter_dictionary:
        meter_dist = to_meter_dictionary[user_unit] / from_meter_dictionary[user_final_unit]
        meter_dist = round(meter_dist, 2)


        print(f"Your distance is: {meter_dist} {user_final_unit}.  ")


    else:
        print('That is not a valid unit of measurement. Please try again.')

    run_again = str.lower(input("Would you like to run this again?  >  "))

print('Thanks for using the unit converter.')

