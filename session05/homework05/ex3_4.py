from turtle import *
#1
def draw_square(length, square_colors):
    color(square_colors)
    for j in range(4):
        forward(length)
        right(90)
    # mainloop()
#2
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

mainloop()