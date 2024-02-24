import math as m

degr = int(input())
print(m.radians(degr))

def trapezoid_area(h, a, b):
    return (a + b) / 2 * h

def polygon_area(s, l):
    return (s * l** 2) / (4 * m.tan(m.pi / s))

def parallelogram_area(b, h):
    return b * h