from pykinematics import Robot

"""
- [ ] ベースオブジェクトの作成：インスタンスで確認

"""


def test_instance():
    base_link = Robot()

    assert isinstance(base_link, Robot)


def test_add():
    base_link = Robot()

    base_link.rotx(0, 0, 0)

    assert base_link.components[0].a == 0
