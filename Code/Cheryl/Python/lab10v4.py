#lab 10 version 4 MODE
from statistics import mode

from fractions import Fraction as fr

def data():
    user_input = input('Please enter your data set:   ')
    print("Mode of data set 1 is % s" % (mode(user_input)))
    return

data()

