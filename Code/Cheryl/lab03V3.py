#Grading Lab version 3- add + and - using modulus

user_grade = int(input("Please enter your number grade: > "))

# to add + and -
singles_digit = user_grade % 10
if singles_digit < 4:
    prefix = '-'
elif singles_digit > 6:
    prefix = "+"
else:
    prefix = ''


if user_grade >= 90:
    print(f'Wahoo!!!That\'s an A{prefix}')

elif user_grade >= 80:
    print(f'Nice job! That\'s a B{prefix}')

elif user_grade >= 70:
    print(f'Meh... That\'s a C{prefix}')

elif user_grade >= 60:
    print(f'That\'s a D{prefix}')

else:
    print('Hide your face! That\'s an F')


