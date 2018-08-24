from turtle import *
t= Turtle()
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color_size = len(colors)

for i in range(color_size):
    t.color(colors[i])

    for y in range(i+3):
        t.forward(100)
        t.left(360/(i+3))

mainloop ()

