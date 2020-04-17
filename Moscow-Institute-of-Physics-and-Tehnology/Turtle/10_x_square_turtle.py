import turtle as t

t.shape("turtle")
n = 10
for i in range(10):
    for j in range(4):
        t.forward(40 + n)
        t.right(90)
    t.left(135)
    t.penup()
    t.forward(10)
    t.right(135)
    n += 15
    t.pendown()

