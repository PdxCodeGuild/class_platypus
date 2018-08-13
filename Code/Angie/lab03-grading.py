grade = int(input('What is your number grade?\n'))

if grade > 100:
    print('Impossible, cheater.')
elif grade == 100:
    print('You got a perfect score!')
elif grade >= 90:
    print('You got an A! Great job superstar.')
elif grade >=80:
    print('You got a B!')
elif grade >=70:
    print('You got a C!')
elif grade >=60:
    print('You got a D!')
elif grade >=0:
    print('You got an F! study more')


else:
    print('Impossible, cheater.')