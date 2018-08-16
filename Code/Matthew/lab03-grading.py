

grade = int(input('what is your number grade? '))

postfix = '-' if grade%10 < 5 else '+' if grade%10 > 5 else ''
tens_digit = grade // 10

#          0    1    2    3    4
grades = ['A', 'B', 'C', 'D', 'F', 'F', 'F', 'F', 'F']

print(grades[len(grades)-tens_digit-1])

