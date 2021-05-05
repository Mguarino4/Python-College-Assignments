from math import *


def triangle_area(x1, y1, x2, y2, x3, y3):

    a = (sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2)))
    b = (sqrt(((x3 - x2) ** 2) + ((y3 - y2) ** 2)))
    c = (sqrt(((x1 - x3) ** 2) + ((y1 - y3) ** 2)))

    s = (a + b + c) / 2

    area = sqrt(s * (s - a) * (s - b) * (s - c))

    return area


print(triangle_area(4, 0, 6, 6, 8, 7))