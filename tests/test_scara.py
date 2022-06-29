from pykinematics.samples import SCARA


def test_scara():
    scara = SCARA()

    scara.info()

    assert True


def test_show():
    scara = SCARA()

    scara.show(figname="scara.png")

    assert True
