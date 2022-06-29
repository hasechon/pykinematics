import numpy as np
from pykinematics import Robot
from pykinematics.samples import SCARA
from pykinematics.samples import PUMA

"""
- [x] ベースオブジェクトの作成：インスタンスで確認
- [ ]

"""


def test_instance():
    base_link = Robot()

    assert isinstance(base_link, Robot)


def test_add():
    base_link = Robot()

    base_link.rot(0, 0, 0)

    assert base_link.components[0].a == 0


class TestTransform:
    """
    - [ ] 連続するリンクの同次変換行列
    - [ ] 2つ以上離れたリンク
        - [ ] リンク間
        - [ ] ベースリンクを含む
        - [ ] エンドエフェクタを含む
    - [ ] ベースリンクからエンドエフェクタまでの同次変換行列
    """

    def test_twe_continuous_link(self):
        robot = Robot()
        robot.rot(10, 0, 0)
        robot.rot(0, 0, 0)

        r = robot.transform(1, 2)

        np.testing.assert_allclose(r,
                                   [[1., 0., 0.,  10.],
                                    [0., 1., 0., 0.],
                                    [0., 0., 1., 0.],
                                    [0., 0., 0., 1.]],
                                   rtol=1e-10, atol=0)


class TestFK:
    """
    - [ ] 
    """

    def test_fk(self):
        robot = Robot()
        robot.rot(10, 0, 0)
        robot.rot(0, 0, 0)
        robot.end_efecter(0, 0, 10, 0)

        r = robot.fk([45, 45])

        np.testing.assert_allclose(r,
                                   [],
                                   rtol=1e-10, atol=0)
