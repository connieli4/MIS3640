import turtle
import math

jack =turtle.Turtle()

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)
        t.pensize(6)

def circle(t, r):
    """ In order to create the yinyang I had to start by creating a general circle"""
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)



def yin(t, r):
    """ next I set up another function to create a circle, but this time I made it so r = 180, which is half of 360, making a semicircle"""
    t.circle(50, 180)

def yang(t, r):
    """Then I had to create another semicircle on top, so I moved the pen up"""
    t.penup()
    t.goto(0, 200)
    t.pendown()
    t.circle(50, 180)

def circle1(t, r):
    """Next, I had to create full size circles of a smaller size and in different pixel locations"""
    t.penup()
    t.goto(0, 120)
    t.pendown()
    t.circle(20, 360)


def circle2(t, r):
    t.penup()
    t.goto(0, 20)
    t.pendown()
    t.circle(20, 360)

jack.speed(100)
""" Lastly, I sped up the drawing process because as I re-ran the code over and over I was getting really impatiet waiting for the shapes to be drawn"""
circle(jack, 100)

yin(jack, 100)
yang(jack, 100)
circle1(jack, 100)
circle2(jack, 100)


turtle.mainloop()