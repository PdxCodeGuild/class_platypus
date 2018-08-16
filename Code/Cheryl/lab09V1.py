# Version 1
answer = 'yes'

while answer == 'yes':
    user_input = float(input("Please enter the number of feet you'd like to convert to meters. >    "))
    output = user_input * 0.3048
    output = round(output, 3)
    print(output)
    answer = str.lower(input('Would you like to run this converter again? answer \'yes\' or \'no\''))
    # answer = str.lower(answer)

else:
    print('Thanks for using the converter. Please come back again.')