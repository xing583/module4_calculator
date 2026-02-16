import pytest
from app.operation import Operation


@pytest.mark.parametrize("a,b,result", [
    (1, 2, 3),
    (-1, 1, 0),
    (2.5, 0.5, 3.0),
])
def test_add(a, b, result):
    assert Operation.add(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (5, 2, 3),
    (0, 1, -1),
    (2.5, 0.5, 2.0),
])
def test_subtract(a, b, result):
    assert Operation.subtract(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (2, 3, 6),
    (-2, 3, -6),
    (2.5, 2, 5.0),
])
def test_multiply(a, b, result):
    assert Operation.multiply(a, b) == result


@pytest.mark.parametrize("a,b,result", [
    (6, 3, 2),
    (-6, 3, -2),
    (5.0, 2.0, 2.5),
])
def test_divide(a, b, result):
    assert Operation.divide(a, b) == result


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operation.divide(1, 0)
