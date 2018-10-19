def rememberer(thing):
    with open('database.txt', 'a') as file:
       file.write(thing+'\n')


if __name__ == '__main__':
    rememberer(input('What should I remember? '))


#     Less efficient way of doing this
# def rememberer(thing):
#     file = open('database.txt', 'a')
#     file.write(thing+'\n')
#     file.close()
#
# if __name__ == '__main__':
#     rememberer(input('What should I remember? '))