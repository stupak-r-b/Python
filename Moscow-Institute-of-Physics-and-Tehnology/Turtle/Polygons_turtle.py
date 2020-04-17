import turtle

def polygon(x_polygons):
    n = 3; size = 20; x = 3
    turtle.shape("turtle")
    for i in range(x_polygons):
        angle = 360 / n
        for j in range(n):
            turtle.forward(size)
            turtle.right(angle)
        n += 1; size += 10
        turtle.left(135)
        turtle.penup()
        turtle.forward(8 + x)
        turtle.right(135)
        turtle.pendown()


polygon(10)