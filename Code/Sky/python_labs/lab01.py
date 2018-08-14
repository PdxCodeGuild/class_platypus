#Turtle Stick Figure
#By Skyler Parker
#Created on 13AUG18

from turtle import *

##### Define Variable #####

#Start Angles
startAngle = 90
startlength = 150

#Head Angles

headAngle = 350
headLength = 10
headColor = 'red'

#body lengths
neckLength = 35
bodyLength = 80
legLength = 45
legAngle = 45
armLength = 35
armAngle = 45

##### Define Functions #####

def draw_stick_figure(headLength, headColor, neckLength, bodyLength, legLength, legAngle, armLength, armAngle):
    # Move to starting location
    penup()
    left(startAngle)
    forward(startlength)
    right(startAngle)
    pendown()

    # Make Head
    angle = 350
    i = 0
    fillcolor(headColor)
    begin_fill()

    while i < 36:
        forward(headLength)
        right(10)
        i += 1
        angle -= 10

    end_fill()
    penup()
    forward(headLength / 2)
    right(90)
    forward(headLength * 36 / 3.14)

    # Make Neck
    pendown()
    forward(neckLength)

    # Make Body
    forward(bodyLength)

    # Make Left Leg
    right(legAngle)
    forward(legLength)
    right(180)
    forward(legLength)
    right(180 - legAngle)

    # Make Right Leg
    left(legAngle)
    forward(legLength)
    left(180)
    forward(legLength)
    left(180 - legLength)

    # Move Cursor
    left(180)
    forward(bodyLength)
    left(180)

    # Make Left Arm
    right(armAngle)
    forward(armLength)
    right(180)
    forward(armLength)
    right(180 - armAngle)

    # Make Right Arm
    left(armAngle)
    forward(armLength)
    left(180)
    forward(armLength)
    left(180 - armLength)


##### Begin Code #####
answer = input('Would you like to input your own dimensions? yes or no.')

if answer == 'no':
    draw_stick_figure(headLength, headColor, neckLength, bodyLength, legLength, legAngle, armLength, armAngle)
elif answer == 'yes':
    headLength = int(input('Head Length?'))
    headColor = input('Head color?')
    neckLength = int(input('Neck Length?'))
    bodyLength = int(input('Body Length?'))
    legLength = int(input('Leg Length?'))
    legAngle = int(input('Leg Angle?'))
    armLength = int(input('Arm Length?'))
    armAngle = int(input('Arm Angle?'))
    draw_stick_figure(headLength, headColor, neckLength, bodyLength, legLength, legAngle, armLength, armAngle)
else:
    print("It needs to be answered yes or no, please restart program")




done()
