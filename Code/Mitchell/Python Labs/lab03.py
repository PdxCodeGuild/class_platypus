numberGrade = input('Please enter a grade percentage from 0 - 100:')
number = int(numberGrade)

if number > 100 or number < 0:
    print('Error: Grade percentage entered is not between 0 and 100')
if number <= 59:
    print('Your score would recieve a letter grade of a F.')
if 60 <= number <= 69:
    print('Your score would recieve a letter grade of a D.')
if 70 <= number <= 79:
    print('Your score would recieve a letter grade of a C.')
if 80 <= number <= 89:
    print('Your score would recieve a letter grade of a B.')
if 90 <= number <= 100:
    print('Your score would recieve a letter grade of an A.')