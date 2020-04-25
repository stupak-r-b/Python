from graph import *


def main():
    moveForward = 0
    while True:
        window_size(1000, 700)
        sky([113, 225, 208], 1000, 700)
        sea([53, 53, 238], [0, 300, 1000, 700])
        beach([242, 248, 16], [0, 470, 1000, 700])
        sun([242, 248, 16], [900, 100, 50])
        cloud([255, 255, 255], 30, [350 + moveForward * 0.1, 50])
        cloud([255, 255, 255], 20, [150, 100])
        boat([50 + moveForward * 0.1, 310], 10, "red")
        boat([150 + moveForward, 345], 30, "brown")
        umbrella(6, [150, 650])
        umbrella(3, [300, 580])
        moveForward += 2

def window_size(width: int , height: int):
    windowSize(width, height)
    canvasSize(width, height)

def sky(color, wigth: int, height: int):
    if type(color) == list:
        r, g ,b = color
    else: color
    brushColor(r, g, b)
    rectangle(0, 0, wigth, height)

def sea(color, location_size: list):
    if type(color) == list:
        r, g, b = color
    else:
        color
    x1, y1, x2, y2 = location_size
    penColor(r, g, b)
    brushColor(r, g, b)
    rectangle(x1, y1, x2, y2)

def beach(color, location_size: list):
    if type(color) == list:
        r, g, b = color
    else:
        color
    x1, y1, x2, y2 = location_size
    penColor(r, g, b)
    brushColor(r, g, b)
    rectangle(x1, y1, x2, y2)

def sun(color, location_size: list):
    if type(color) == list:
        r, g, b = color
    else:
        color
    x, y, radius = location_size
    penColor(r, g, b)
    brushColor(r, g, b)
    circle(x, y, radius)

def cloud(color, size: list, location: list):
    def part_of_cloud(location: list, size, color):
        x, y = location
        if type(color) == list:
            r, g, b = color
        else: color
        penColor(172, 172, 172)
        brushColor(r, g, b)
        circle(x, y, size)

    if type(color) == list:
        r, g, b = color
    else:
        color
    x, y = location
    part_of_cloud([x - size * 0.5, y + size], size, color)
    part_of_cloud([x + size * 0.8, y + size], size, color)
    part_of_cloud([x + size * 1.9, y + size], size, color)
    part_of_cloud([x + size * 2.9, y + size], size, color)
    part_of_cloud([x, y], size, color)
    part_of_cloud([x + size * 1.2, y], size, color)
    part_of_cloud([x + size * 2.3, y], size, color)


def boat(location: list, size: list, color):
    def back_end(size, color, location):
        if type(color) == list:
            r, g, b = color
        else: color
        brushColor(color)
        penColor(color)
        x, y = location
        radius = size
        circle(x, y, radius)

        #  boat (the back is covered by a blue rectangle)
        penColor(53, 53, 238)
        brushColor(53, 53, 238)
        rectangle(x - radius, y - radius, x + radius, y)


    def central_part(size: list, color, location):
        if type(color) == list:
            r, g, b = color
        else: color
        x, y = location
        penColor(color)
        brushColor(color)
        rectangle(x, y + 1, x + size * 5.5, y + size)

    def front_part(size, color, location):
        if type(color) == list:
            r, g, b = color
        else: color
        penColor(color)
        brushColor(color)
        x, y = location
        polygon([(x + size * 5.5, y + size), (x + size * 5.5 , y + 1), (x + size * 8, y)])


    def parthole(location, size):
        x , y = location
        x = x - 0.8 * size
        item = 20
        penColor("black")
        times = 6 if size > 15 else 4
        for i in range(times):
            color = "white" if size < 25 else "black"
            brushColor(color)
            circle(x + item, y + size / 2, size / 5)
            brushColor("white")
            circle(x + item, y + size / 2 , size / 6.5)
            item += size * 1.1


    def mast(size, color, location):
        if type(color) == list:
            r, g, b = color
        else: color
        penColor("black")
        brushColor("black")
        penSize(size // 5)
        x, y = location
        line(x + size * 1.97, y, x + size * 1.97, y - size * 3.5)
        penSize(1)

    def mast_sail(size, color, location):
        if type(color) == list:
            r, g, b = color
        else: color
        penColor(172, 172, 172)
        brushColor(239, 228, 176)
        x, y = location
        polygon([(x + size * 2.05, y - size * 3.5), (x + size * 4.2, y - size * 1.88), (x + size * 2.65, y - size * 1.88)])
        polygon([(x + size * 2.05, y, x + size * 1.97), (x + size * 4.2, y - size * 1.88), (x + size * 2.65, y - size * 1.88)])

    back_end(size, color, location)
    central_part(size, color, location)
    front_part(size, color, location)
    mast(size, color, location)
    mast_sail(size, color, location)
    parthole(location, size)


def umbrella(size: int, location: list):
    penColor("brown")
    brushColor("brown")
    penSize(size * 2)
    x, y = location
    line(x, y - size * 5, x, y - size * 45)

    penColor(237, 28, 36)
    brushColor(243, 112, 118)
    penSize(1)
    item = size * 5
    for i in range(8):
        polygon([(x + size, y - size * 52), (x - size * 25 + item, y - size * 43), (x - size * 18 + item, y - size * 43)])
        item += size * 5


main()
