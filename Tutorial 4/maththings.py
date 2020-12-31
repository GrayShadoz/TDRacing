from math import *


def get_angle_between(point1, point2):
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    angle = atan2(dy, dx)
    return angle