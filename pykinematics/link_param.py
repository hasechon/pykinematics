from enum import Enum


class Direction(Enum):
    ROT = 1
    LINEAR = 2
    BASE = 3
    ENDEFECTER = 4


class LinkParameter:
    def __init__(self, direction, a, alpha, d, theta):
        self.a = a
        self.alpha = alpha
        self.d = d
        self.theta = theta

        self.direction = direction

    def __str__(self):
        if self.direction == Direction.ROT:
            # 回転関節
            d = self.d
            theta = "q"
        elif self.direction == Direction.LINEAR:
            # 直動関節
            d = "q"
            theta = self.theta
        elif self.direction == Direction.BASE:
            # リンク0 ベース部分
            d = "-"
            theta = "-"
        elif self.direction == Direction.ENDEFECTER:
            # エンドエフェクタ
            d = "-"
            theta = "-"
        else:
            print(self.direction)
            raise
        return "{},{:>5},{:>5},{:>5},{:>5}".format(self.direction, self.a, self.alpha, d, theta)
