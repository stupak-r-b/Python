import turtle as t


def flower(x_petal):
    t.shape("turtle")
    n = 2
    while True:
        for i in range(180):
            t.forward(3)
            t.right(n)
        n *= -1
        t.left(360/x_petal)

flower(360)