## this program draws a flower in python
import turtle
import math

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    ## initialize constant factor that will be
    ## the equal legs of the Isosceles Triangle
    constant_factor = 100
    counter2 = 0
    ## make triangle 20 times
    while counter2 < 20:

        ## create an Isosceles triangle
        brad.forward(constant_factor * math.sqrt(2) / 2)
        brad.right(135)
        brad.forward(constant_factor)
        brad.right(90)
        brad.forward(constant_factor)
        brad.right(135)
        brad.forward(constant_factor * math.sqrt(2) / 2)

        ## turn 18 degrees (this will happen 20x for
        ## a total of 360 degrees)
        brad.right(18)
        counter2 += 1

    #angie = turtle.Turtle()
    #angie.shape("arrow")
    #angie.color("blue")
    #angie.circle(100)

    #jenny = turtle.Turtle()
    #jenny.shape("arrow")
    #jenny.color("yellow")
    #counter0 = 0
    #while counter0 < 3:
    #    jenny.forward(150)
    #    jenny.right(120)
    #    counter0 += 1

    ## make stem
    brad.right(90)
    brad.forward(250)
    window.exitonclick()

draw_square()
