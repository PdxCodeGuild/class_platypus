#lab 3 grading version 2. adding + and - to the grades.

grade = int(input("Please enter your number grade here: >  "))

if grade > 97:
    print('That\'s an A+')
elif grade > 92 and grade < 98:
    print('That\'s an A')
elif grade <93 and grade > 89:
    print('That\'s an A-')

elif grade > 87 and grade < 90:
    print('That\'s a B+')
elif grade > 82 and grade < 88:
    print('That\'s a B')
elif grade < 83 and grade > 79:
    print('That\'s a B-')

elif grade > 77 and grade < 80:
    print('That\'s a C+')
elif grade > 72 and grade < 78:
    print('That\'s a C')
elif grade < 73 and grade > 69:
    print('That\'s a C-')

elif grade < 70 and grade > 59:
    print('That\'s a D')
else:
    print('That\'s an F')
