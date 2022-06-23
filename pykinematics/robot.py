
from .link_param import LinkParameter, Direction


class Robot():
    def __init__(self):
        self.components = []

    def rotx(self, a, alpha, d):
        self.components.append(LinkParameter(Direction.ROTX, a, alpha, d, 0))

        return self

    def liner(self, a, alpha,  theta):
        self.components.append(LinkParameter(
            Direction.LINEAR, a, alpha, 0, theta))

        return self
