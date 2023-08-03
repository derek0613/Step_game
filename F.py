from turtle import Screen, Turtle

GRID_SIZE = 600

sub_divisions = int(input("Enter the number of sub-divisions: "))

cell_size = GRID_SIZE / float(sub_divisions)  # force float for Python 2

screen = Screen()

turtle = Turtle()
turtle.penup()
turtle.goto(-GRID_SIZE/2, GRID_SIZE/2)
turtle.pendown()

angle = 90

for _ in range(4):
    turtle.forward(GRID_SIZE)
    turtle.right(angle)

for _ in range(2):
    for _ in range(1, sub_divisions):
        turtle.forward(cell_size)
        turtle.right(angle)
        turtle.forward(GRID_SIZE)
        turtle.left(angle)

        angle = -angle

    turtle.forward(cell_size)
    turtle.right(angle)

from turtle import Screen, Turtle
from random import randrange

PEN_SIZE = 8

def tree(branch_length, turtle, pen_size):
    if branch_length < 5:
        return

    angle = randrange(5, 35)
    double_angle = angle * 2
    sub_length = branch_length - randrange(1, 19)

    turtle.pensize(pen_size)
    pen_size *= 0.8

    turtle.forward(branch_length)
    turtle.right(angle)
    tree(sub_length, turtle, pen_size)
    turtle.left(double_angle)
    tree(sub_length, turtle, pen_size)
    turtle.right(angle)
    turtle.backward(branch_length)

def main():
    myWin = Screen()
    yertle = Turtle(visible=False)

    yertle.left(0)
    yertle.penup()
    yertle.backward(0)
    yertle.pendown()

    myWin.tracer(False)
    #tree(randrange(40, 47), yertle, PEN_SIZE)
    myWin.tracer(True)

    myWin.exitonclick()
 
main()
#import random
#number = random.randint(1, 18)
#counter = 0
#for i in range(1,19):
    #print(i)
