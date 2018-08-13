test_grade = input("What score did you get? >")
test_grade = int(test_grade)
mod= '-' if test_grade < 5 else '+' if test_grade %10 > 5 else ''

if test_grade <= 59:
    print('F' + mod)
if (test_grade >= 60 and test_grade <= 69):
    print('D' + mod)
if (test_grade >= 70 and test_grade <= 79):
    print('C' + mod)
if (test_grade >= 80 and test_grade <= 89):
    print('B' + mod)
if (test_grade >= 90 and test_grade <= 100):
    print('A' + mod)
