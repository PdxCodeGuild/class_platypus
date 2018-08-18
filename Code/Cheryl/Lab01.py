
#Lab 01

from turtle import *

head = 0
while head <= 21:
    forward(20)
    right(25)
    head += 1

left(100)
forward(40)
right(110)
forward(80)
right(180)
forward(80)

#right arm
left(45)
forward(80)
left(180)
forward(80)

#body
left(66)
forward(95)

#left leg
right(40)
forward(60)
right(180)
forward(60)

#right leg
right(90)
forward(60)
right(180)
forward(60)

done()