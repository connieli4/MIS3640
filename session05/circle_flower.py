import turtle
import math

def polygon(t, n, length):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)

def circle(t, r):
# """I started off by creating a normal circle"""
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

def petal(t, r, angle):
# """Next I created the petals by creating more circles, but moving the pen at a left 180 degree angle at the radius to kind of distort the shape"""
    for i in range(2):
        t.circle(r, angle)
        t.lt(180-angle)

def flower(t, n, r, angle):
# """Lastly, I had to move the flower up because it was not in the center of the circle"""
    for i in range(n):
        t.penup()
        t.goto(0, 100)
        t.pendown()
        petal(t, r, angle)
        t.lt(360/n)
        


jack= turtle.Turtle()

jack.speed(100)
circle(jack, 100)
flower(jack, 7, 80, 80)

turtle.mainlook()