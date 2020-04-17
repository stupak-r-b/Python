import turtle as t

def spring(x_time):
    t.shape("turtle")
    t.left(90)
    for i in range(x_time):
        for j in range(90):
            t.forward(2)
            t.right(2)
        if i < x_time-1:
            for k in range(45):
                t.forward(0.7)
                t.right(4)

spring(3)