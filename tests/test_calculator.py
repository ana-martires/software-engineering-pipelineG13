from calculator import add, sub, sqrt
from calculator import add, sub, factorial
from calculator import add, sub, squared
from calculator import add, sub, factorial, division, multiply, squared, power


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(10, 4) == 6

def test_sqrt():
    assert sqrt(81) == 9
    assert sqrt(16) == 4

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_division():
    assert division(4, 2) == 2


def test_multiply():
    assert multiply(2, 5) == 10


def test_squared():
    assert squared(4) == 16
    assert squared(0) == 0
    assert squared(-3) == 9


def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(4, 2) == 16
