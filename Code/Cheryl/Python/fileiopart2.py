# Note: this will only run on command line

import sys

def rememberer(thing):
    with open('database.txt', 'a') as file:
        file.write(thing+'\n')


def show():
    with open('database.txt') as file:
        for line in file:
            print(line)



if __name__ == '__main__':
    if sys.argv[1].lower() == '--list':
        show()

    else:
        # grabs all arguments after the position 0, which is the python file
        rememberer(' '.join(sys.argv[1:]))