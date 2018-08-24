from turtle import *
t= Turtle()
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color_size = len(colors)

for i in range(1, color_size):
    t.color(colors[i])
    t.begin_fill()      
    x = 50
    for y in range(i):
        for z in range (1,4):
            if z % 2 == 0:
                forward(x*i)
            else:
                forward(100)
        right(90)          
    t.end_fill()
    x += 50
    
mainloop ()