# Exercise 2
# Write a definition for a class named Circle with attributes center and radius, where center is a Point object and radius is a number.

# Instantiate a Circle object that represents a circle with its center at (150, 100) and radius 75.

# Write a function named point_in_circle that takes a Circle and a Point and returns True if the Point lies in or on the boundary of the circle.

# Write a function named rect_in_circle that takes a Circle and a Rectangle and returns True if the Rectangle lies entirely in or on the boundary of the circle.

# Write a function named rect_circle_overlap that takes a Circle and a Rectangle and returns True if any of the corners of the Rectangle fall inside the circle. Or as a more challenging version, return True if any part of the Rectangle falls inside the circle.

class Point:
    """Represents a point in 2-D space.

    attributes: x, y
    """

class Circle:
    center = Point()


original_circle = Circle()
original_circle.x = 150
original_circle.y = 100
original_circle.radius = 75
# print('The circle has a center point of ({}, {})'.format(original_circle.x, original_circle.y))
# print('and a radius of', original_circle.radius)

import math

def point_in_circle(px, py):
    my_point = Point()
    my_point.x = px
    my_point.y = py
    diff_x = my_point.x-original_circle.x
    diff_y = my_point.y - original_circle.y
    new_radius = math.sqrt(diff_x**2 + diff_y**2)
    if new_radius <= original_circle.radius:
        return True
    else:
        return False

# print(point_in_circle(149,100))

class Rectangle:
    """Represents a rectangle. 

    attributes: width, height, corner.
    """

def rect_in_circle(rect, bwidth, bheight):
    my_box = Point()
    rect = Rectangle()
    rect.width = bwidth
    my_box.height = bheight
    rect.corner.x = bx + bwidth
    rect.corner.y = by + bheight
    corner_distance_x = my_box.corner.x - original_circle.x
    corner_distance_y = my_box.corner.y - original_circle.y
    center_distance_x = my_box.x - original_circle.x
    center_distance_y = my_box.y - original_circle.y
    r1 = math.sqrt(corner_distance_x**2 + corner_distance_y**2)
    r2 = math.sqrt(center_distance_x**2 + center_distance_y**2)
    if (r1 <= original_circle.radius) and (r2 <= original_circle.radius):
        return True
    else:
        return False

print(rect_in_circle(120, 70, 13, 22))