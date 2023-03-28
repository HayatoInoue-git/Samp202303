'''import turtle

turtle.penup()
turtle.goto(-50, 0)
turtle.pendown()
turtle.forward(50)
turtle.right(90)
turtle.forward(10)
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(10)
turtle.left(90)
turtle.forward(50)
'''

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()