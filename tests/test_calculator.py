from calculator import add, sub, squared

def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6

def test_squared():
    assert squared(4) == 16
    assert squared(0) == 0
    assert squared(-3) == 9

