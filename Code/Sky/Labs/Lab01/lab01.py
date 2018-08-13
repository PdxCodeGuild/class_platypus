#Turtle Stick Figure
#By Skyler Parker
#Created on 13AUG18

from turtle import *

#Start Angles
startAngle = 90
startlength = 150

#Head Angles

headAngle = 350
headLength = 10

#body lengths
neckLength = 35
bodyLength = 80
legLength = 45
legAngle = 45
armLength = 35
armAngle = 45



penup()
left(startAngle)
forward(startlength)
right(startAngle)
pendown()


#Make Head
angle = 350
i = 0
while i < 36:
    forward(headLength)
    left(headAngle)
    i += 1
    angle -= 10

penup()
forward(headLength/2)
right(90)
forward(115)

#Make Neck
pendown()
forward(neckLength)

#Make Body
forward(bodyLength)

#Make Left Leg
right(legAngle)
forward(legLength)
right(180)
forward(legLength)
right(180-legAngle)

#Make Right Leg
left(legAngle)
forward(legLength)
left(180)
forward(legLength)
left(180-legLength)

#Move Cursor
left(180)
forward(bodyLength)
left(180)

#Make Left Arm
right(armAngle)
forward(armLength)
right(180)
forward(armLength)
right(180-armAngle)

#Make Right Arm
left(armAngle)
forward(armLength)
left(180)
forward(armLength)
left(180-armLength)


done()
