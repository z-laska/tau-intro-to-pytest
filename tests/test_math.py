import pytest


def test_one_plus_one():
    assert 1 + 1 == 2


def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0

    assert 'division by zero' in str(e.value)


products = [
    (2, 3, 6),  # positive integers
    (1, 99, 99),  # identity
    (0, 99, 0),  # zero
    (3, -4, -12),  # positive by negative
    (-5, -5, 25),  # negative by negative
    (2.5, 6.7, 16.75)  # floats
]


@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert a * b == product
