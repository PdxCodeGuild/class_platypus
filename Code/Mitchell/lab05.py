import random
eyes = [':', ';', '8', '=']
nose = ['^', 'c', '>', '-', '*', 'v']
mouth = [')', '|', '(', 'P', 'O', '/', ']']
oneOrFive = input('Do you want to generate 1 or 5 random emoticons? (type 1 or 5)')
if oneOrFive != '1' and oneOrFive != '5':
    print('ERROR: You entered something that was not "1" or "5"')
if oneOrFive == '1':
    print('Here is 1 randomly generated emoticon:  ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth))
if oneOrFive == '5':
    print('Here is 5 randomly generated emoticons:  ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth) +
    '   ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth) + '  '
    '   ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth) + '  '
    '   ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth) + '  '
    '   ' + random.choice(eyes) + ' ' + random.choice(nose) + ' ' + random.choice(mouth) + '  ')