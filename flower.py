import turtle
from random import randint, gauss, choice
import numpy as np


turtle.speed(8)
nr_flowers = 28

# Array with possible locations of the flower
Locations = np.zeros((28,2))
for i in range(28):
    if i<7:
        Locations[i,1] = 260 + 20*i
        Locations[i,0] = -600 + 180*i
    elif i<14:
        Locations[i, 1] = 70 + 20*(i-7)
        Locations[i, 0] = -600 + 180*(i-7)
    elif i<21:
        Locations[i, 1] = -70 + 20*(i-14)
        Locations[i, 0] = -600 + 180* (i - 14)
    else:
        Locations[i, 1] = -260 + 20*(i-21)
        Locations[i, 0] = -600 + 180 * (i - 21)
choose_location = np.random.choice(28, size=nr_flowers, replace=False, p=None)
# print(choose_location)

def my_flower(turtle, SIZE):
    color = "#" + ''.join([choice('0123456789ABCDEF') for j in range(6)])
    turtle.pencolor(color)
    nr_points = [5,7,9,11,13,15,17]
    index = randint(0,6)
    points = nr_points[index]
    ANGLE = 360/points*(index+2)
    for i in range(points):
        turtle.forward(SIZE)
        turtle.left(ANGLE)


for i in range(nr_flowers):
    turtle.penup()
    turtle.goto(Locations[choose_location[i], :])
    turtle.pendown()
    SIZE = randint(50,300)
    my_flower(turtle, SIZE)



turtle.done()
