from ..robot import Robot


class PUMA(Robot):
    def __init__(self):
        super().__init__()

        self.rot(0, 0, 0)
        self.rot(0, -90, 10)
        self.rot(30, 0, 0)
        self.rot(10, -90, 20)
        self.rot(0, 90, 0)
        self.rot(10, -90, 0)
