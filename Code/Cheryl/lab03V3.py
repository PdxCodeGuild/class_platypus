#Grading Lab version 3- add + and - using modulus

user_grade = int(input("Please enter your number grade: > "))

# to add + and -

singles_digit = user_grade % 10
if singles_digit < 5:
    prefix = '-'
elif singles_digit > 5:
    prefix = ""


if user_grade >= 90:
    print('Wahoo!!!That\'s an \'A\'' + prefix)

elif user_grade >= 80:
    print('Nice job! That\'s a \'B\'' + prefix)

elif user_grade >= 70:
    print('Meh... That\'s a \'C\'' + prefix)

elif user_grade >= 60:
    print('That\'s a \'D\'' + prefix)

else:
    print('Hide your face! That\'s an \'F\'')


