"""Turtle Tutorials."""

from turtle import Turtle, colormode, done
colormode(255)

leo: Turtle = Turtle()

leo.pencolor(99, 204, 250)
leo.fillcolor(180, 180, 180)
leo.speed(50)
leo.hideturtle()

leo.penup()
leo.goto(-150, -130)
leo.pendown()

leo.begin_fill()
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()

bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.speed(1000)
bob.hideturtle()

bob.penup()
bob.goto(-150, -130)
bob.pendown()
i = 0
while i < 3:
    bob.forward(300)
    bob.left(120)
    i += 1

side_length: int = 300
i = 0
while i < 600:
    side_length = side_length * 0.99
    bob.forward(side_length)
    bob.left(123)
    i += 1

done()