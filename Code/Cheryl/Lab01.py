
#Lab 01

from turtle import *

length = 100
neck_length = 30
body_length = 200
hand_length = 50
angle = 90
angle2 = 270
head = 0
body = 0
hand = 0
star_angle = 144

#head
fillcolor('pink')
begin_fill()

while head < 4:
    forward(length)
    left(angle)
    head += 1

end_fill()

#neck
setposition(50, 0)
left(angle2)
forward(neck_length)

#body
fillcolor('purple')
begin_fill()

right(angle)
forward(100)
while body < 3:
    left(angle)
    forward(body_length)
    body += 1
left(angle)
forward(100)
end_fill()

#right arm
left(180)
forward(100)
right(90)
forward(30)
left(90)
forward(50)
right(85)
forward(75)

#right hand

fillcolor('green')
begin_fill()
while hand < 4:
    forward(30)
    left(angle)
    hand += 1

end_fill()

#right hand fingers
forward(70)

left(angle)
forward(5)
left(angle)
forward(50)
#finger2
right(angle)
forward(5)
right(angle)
forward(50)
left(angle)
forward(5)
left(angle)
forward(50)

#finger three
right(angle)
forward(5)
right(angle)
forward(50)
left(angle)
forward(5)
left(angle)
forward(50)



#move to left side

forward(20)
left(angle)
forward(25)
right(angle)
forward(75)
left(angle)
forward(50)
right(95)
forward(35)
left(angle)
forward(200)

#left arm
left(90)
forward(25)
right(90)
forward(30)
left(90)
forward(50)
right(85)
forward(75)

left_hand = 0
fillcolor('green')
begin_fill()
while left_hand < 4:
    left(angle)
    forward(30)
    left_hand += 1

end_fill()

#left hand fingers
forward(25)

left(angle)
forward(15)
left(angle)
forward(30)
#finger2
right(angle)
forward(5)
right(angle)
forward(50)
left(angle)
forward(5)
left(angle)
forward(50)

#finger three
right(angle)
forward(5)
right(angle)
forward(50)
left(angle)
forward(5)
left(angle)
forward(75)

#go to leg area
left(angle)
forward(35)
right(angle)
forward(80)
left(angle)
forward(10)

done()