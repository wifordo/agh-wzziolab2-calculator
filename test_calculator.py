# test_calculator.py
import pytest
from calculator import Calculator

@pytest.mark.parametrize("a,b,expected", [
    (3, 2, 5),
    (0, 0, 0),
    (-1, 1, 0),
    (2.5, 1.5, 4.0),
])
def test_sum(a, b, expected):
    calc = Calculator(a, b)
    assert pytest.approx(calc.sum(), rel=1e-12) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 0, 0),
    (-1, -1, 0),
    (2.5, 1.0, 1.5),
])
def test_subtract(a, b, expected):
    calc = Calculator(a, b)
    assert pytest.approx(calc.subtract(), rel=1e-12) == expected

@pytest.mark.parametrize("a,b,expected", [
    (4, 3, 12),
    (0, 5, 0),
    (-2, -3, 6),
    (2.5, 2, 5.0),
])
def test_multiply(a, b, expected):
    calc = Calculator(a, b)
    assert pytest.approx(calc.multiply(), rel=1e-12) == expected

@pytest.mark.parametrize("a,b,expected", [
    (10, 2, 5),
    (5.5, 2.2, 5.5/2.2),
    (-6, -2, 3),
])
def test_divide(a, b, expected):
    calc = Calculator(a, b)
    assert pytest.approx(calc.divide(), rel=1e-12) == expected

def test_divide_by_zero_raises():
    calc = Calculator(10, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide()

def test_constructor_casts_to_float():
    # Opcjonalne: jeśli konstruktor rzutuje stringi na float
    calc = Calculator(1, "2")
    assert pytest.approx(calc.sum(), rel=1e-12) == 3.0

def test_small_values():
    a = 1e-10
    b = 1e-12
    calc = Calculator(a, b)
    assert pytest.approx(calc.sum(), rel=1e-9) == a + b
