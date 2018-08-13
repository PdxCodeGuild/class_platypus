import random
response = ['it is certain','without a doubt','go girl','not a good idea','may not be a good time','wait till next month','something is brewing','worst possible choice','NO','donot even thin about it!']

keep_asking = 'yes'
while keep_asking == 'yes':
    input ('Ask magic ball a question: ')
    print( f"{random.choice(response)}.")
    keep_asking = input('ask another question? ')

