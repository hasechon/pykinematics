from enum import Enum


class Direction(Enum):
    LINEAR = 1
    ROTX = 2
    ROTY = 3
    ROTZ = 4


class LinkParameter:
    def __init__(self, direction, a, alpha, d, theta):
        self.a = a
        self.alpha = alpha
        self.d = d
        self.theta = theta

        self.direction = direction
