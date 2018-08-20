#lab 19 blackjack version 1
user_choice = []
user_choice = input('Please choose three cards:\n A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K, \nand I will give you advice on whether or not to\n \'Hit\', \'Stay\', or if you\'ve already \'Busted\' >   ').lower()


cards_info = {'a': 1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'j':10, 'q':10, 'k':10}

for i in user_choice.split():
    i.strip()




print(user_choice)