from ..robot import Robot


class SCARA(Robot):
    def __init__(self):
        super().__init__()

        self.rot(0, 0, 0)
        self.rot(0, -90, 0)
        self.rot(10, 0, 0)
