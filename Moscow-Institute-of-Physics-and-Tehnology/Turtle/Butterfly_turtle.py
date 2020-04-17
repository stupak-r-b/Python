import turtle as t

def butterfly():
    t.shape("turtle")
    diameter = 1
    t.penup()
    for i in range(45): t.forward(3); t.right(2)
    t.pendown()
    while True:
        for j in range(2):
            for i in range(180):
                t.forward(diameter)
                t.right(2)
            t.right(180)
        diameter += 0.2

butterfly()