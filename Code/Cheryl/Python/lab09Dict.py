#same as v4 but using dictionaries NEED TO FINISH!!!

welcome_mess = print('Welcome to the unit converter.')

meter_dist = 0
run_again = 'yes'

user_unit = 0


while run_again == 'yes':

    user_unit = str.lower(input('What unit would you like to convert FROM: ft, mi, m, yds, in, or km.  >   '))

    user_final_unit = str.lower(input('What unit would you like to convert TO: ft, mi, m, yds, in, or km.  >   '))

    user_dist = float(input(f'Please enter the distance you would like to convert from {user_unit}.  >   '))

    user_dist = round(user_dist, 2)

    to_meter_dictionary = {'km': user_dist * 1000, 'ft': user_dist * .3048}
    from_meter_dictionary = {'km': user_dist / 1000, 'ft': user_dist / .3048}



    if user_unit in to_meter_dictionary:
        to_meter_dictionary[user_unit] += 1
    else:
        to_meter_dictionary[user_unit] = 1

    print(from_meter_dictionary)
    print(f"Your distance is: {meter_dist} {user_final_unit}.  ")
    run_again = str.lower(input("Would you like to run this again?  >  "))



print('Thanks for using the unit converter.')
