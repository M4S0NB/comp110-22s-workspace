"""My beautiful Turtle Painting.

I used a function from the webpage to create circles in lines 43 and 69.
I also used a function from the webpage to create a background in line 12.
"""

__author__ = "730481220"

from turtle import Turtle, bgcolor, colormode, done

colormode(255)
bgcolor(2, 222, 225)


def ground() -> None:
    """Function creating the bricks the old well sits on."""
    ground: Turtle = Turtle()
    ground.color(199, 93, 50)
    ground.hideturtle()
    ground.speed(300)
    ground.penup()
    ground.goto(-375, -265)
    ground.pendown()
    i: int = 0
    ground.begin_fill()
    while i < 4:
        ground.forward(750)
        ground.right(90)
        i += 1
    ground.end_fill()


def sun() -> None:
    """Function drawing the beautiful sun."""
    sun: Turtle = Turtle()
    sun.color(239, 238, 14)
    sun.speed(300)
    sun.hideturtle()
    sun.penup()
    sun.goto(-350, 250)
    sun.pendown()
    sun.begin_fill()
    sun.circle(100, None, None)
    sun.end_fill()


def rectangle(color: Turtle, x_position: int, y_position: int, relative_size: float) -> None:
    """Function I used to draw all of my vertical rectangles."""
    color.penup()
    color.goto(x_position, y_position)
    color.pendown()
    color.begin_fill()
    i = 0
    while i < 2:
        color.forward(25 * relative_size)
        color.left(90)
        color.forward(300 * relative_size)
        color.left(90)
        i += 1
    color.end_fill()


def leaves(color: Turtle, x_position: int, y_position: int) -> None:
    """Function to draw the leaves of trees."""
    color.penup()
    color.goto(x_position, y_position)
    color.pendown
    color.begin_fill()
    color.circle(130, None, None)
    color.end_fill()


def old_well(color: Turtle, x_position: int, y_position: int) -> None:
    """Very long function for all of the parts of the old well except the fountain."""
    color.penup()
    color.goto(x_position - 200, y_position + 20)
    color.pendown()
    # the pillars of the old well
    rectangle(color, x_position - 75, y_position + 20, .5)
    rectangle(color, x_position - 25, y_position + 20, .5)
    rectangle(color, x_position + 25, y_position + 20, .5)
    rectangle(color, x_position + 75, y_position + 20, .5)
    color.penup()
    color.goto(107, -140)
    color.left(90)
    color.pendown()
    color.begin_fill()
    # the top of the old well
    color.circle(100, 180, 90)
    color.end_fill()
    color.penup()
    color.goto(x_position - 75, y_position + 20)
    color.pendown()
    i = 0
    color.begin_fill()
    # first stair of the old well
    while i < 2:
        color.left(90)
        color.forward(150)
        color.left(90)
        color.forward(10)
        i += 1
    color.end_fill()
    color.penup()
    color.goto(x_position - 92, y_position + 10)
    color.pendown()
    # second stair of the old well
    i = 0
    color.begin_fill()
    while i < 2:
        color.left(90)
        color.forward(200)
        color.left(90)
        color.forward(10)
        i += 1
    color.end_fill()


def fountain(color: Turtle, x_position: int, y_position: int) -> None:
    """Function used for drawing the fountain."""
    # I made this seperate from the old well function because it was a last second add on and I would've had to change alot to fit it in on the old well function.
    color.penup()
    color.goto(x_position, y_position)
    color.pendown()
    color.begin_fill()
    # Trapezoid geometry
    color.forward(15)
    color.left(80)
    color.forward(30)
    color.left(100)
    color.forward(25)
    color.left(100)
    color.forward(30)
    color.end_fill()


def main() -> None:
    """The entrypoint of my scene."""
    brown: Turtle = Turtle()
    brown.color(139, 88, 48)
    brown.speed(300)
    brown.hideturtle()
    green: Turtle = Turtle()
    green.color(58, 161, 21)
    green.speed(300)
    green.hideturtle()
    white: Turtle = Turtle()
    white.color(255, 255, 255)
    white.speed(300)
    white.hideturtle()
    grey: Turtle = Turtle()
    grey.color(116, 137, 139)
    grey.speed(10)
    grey.hideturtle()
    ground()
    sun()
    rectangle(brown, 200, -300, 1.25)
    rectangle(brown, -200, -300, 1.0)
    rectangle(brown, 100, -275, .80)
    leaves(green, -185, -40)
    leaves(green, 215, -20)
    leaves(green, 115, -100)
    old_well(white, 0, -300)
    fountain(grey, 0, -270)


if __name__ == "__main__":
    main()
done()