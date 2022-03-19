""" This program uses the turtle library to draw a flower.
The flower shall has 4 petals and 1 stamen (the center of the flower).
The screen background color for this program is black
 The petals of the flower are yellow in color
 The stamen of the flower is red in color
 Input = this program takes no input from the user
 Output = this program uses a speed of 1000 to draw a flower to the screen using the turtle library"""

import turtle
from turtle import *

def petals():
    turtle.bgcolor("black")  # changes the background color from white to black
    turtle.color("yellow")  # draws the petals of the flower in yellow
    turtle.speed(1000)  # gives the speed at which the turtle draws
    for i in range(187):  # gives the number of times it would draw the shape that makes the petals
        circle(190-i, 90)
        left(90)
        circle(190 - i, 90)
        left(18)
    stamen()  # calls the stamen function

def stamen():
    turtle.speed(1000)  # gives the turtle a drawing speed
    penup()  # takes the pen up while the turtle moves the pointer to the position assigned
    turtle.setposition(-15, 20)  # sets the position where the stamen would start from
    pendown()  # puts the pen down so the stamen drawing shows
    turtle.color("red")  # sets color red for the stamen
    for i in range(70):
        circle(20-i, 180)

petals()

turtle.mainloop()
