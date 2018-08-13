#Letter Grade
#By Skyler Parker
#Created on 13AUG18


appExit = False

while appExit != bool(True):
    menuAnswer = int(input('\nMenu:\n\n1 - Enter a new grade\n2 - Close Program'))

    letterGrade = ''
    suffix = ''

    if menuAnswer == 1:
        grade = int(input('What did you get on the test? '))

        remainder = (int(grade) % 10)
        if remainder <= 3:
            suffix = '-'
        elif remainder >=7:
            suffix = '+'


        if grade > 90:
            letterGrade = 'A'
        elif grade > 80:
            letterGrade = 'B'
        elif grade > 70:
            letterGrade = 'C'
        elif grade > 60:
            letterGrade = 'D'
        else:
            letterGrade = 'F'
            suffix = ''
        print('Your letter grade is a ' + letterGrade + suffix + '!')

    else:
        appExit = bool(True)

