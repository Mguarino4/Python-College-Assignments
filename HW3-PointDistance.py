from math import *

def point_distance(x0, y0, x1, y1):
    return(sqrt(((x1 - x0) ** 2) + ((y1 - y0) ** 2)))

while True:
        x0 = float(input("Enter value for x0: "))
        y0 = float(input("Enter value for y0: "))
        x1 = float(input("Enter value for x1: "))
        y1 = float(input("Enter value for y1: "))
        print(point_distance(x0, y0, x1, y1))