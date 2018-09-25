#lab 10 version 4 MODE
from statistics import mode

from fractions import Fraction as fr

def data():
    try:
        data_set = input('Please enter your data set. >  ')
        data_set = data_set.split(',')
        if data_set == str:
            print('it is a string')
        print("Mode of data set is % s" % (mode(data_set)))
        return
    except ValueError:
        print('There is no mode in this data set.')

data()

