from turtle import *
t= Turtle()
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color_size = len(colors)

for i in range(color_size):
    t.color(colors[i])
    t.begin_fill()      
    x = 50
    for k in range(4):
        if k%2 == 0:
            t.forward(x)
        else:
            t.forward(100)
        t.right(90)

    t.end_fill()
    penup()
    t.forward(50)
    pendown()
    
mainloop ()
