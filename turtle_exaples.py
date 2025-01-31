from turtle import *
"""
#triangle forward()-direction and left() - angle 
forward(100)
left(120)
forward(100)
left(120)
forward(100)

#triangle with backward() and right()
backward(100)
right(120)
backward(100)
right(120)
backward(100)


#pen
penup()
color("red")
forward(100)

color('blue')
width(3)


for steps in range(100):
    for c in ('blue', 'red', 'green'):
        color(c)
        forward(steps)
        right(30)
"""
def draw_star():
    color('red')
    fillcolor('yellow')
    begin_fill()

    while True:
        forward(200)
        left(170)
        if abs(pos()) < 1:
            break
    end_fill()

draw_star()
#mainloop()
