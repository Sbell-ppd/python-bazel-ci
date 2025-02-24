import pytest
from src.math_utils import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(3, 2) == 1
    assert subtract(-1, 1) == -2

def test_multiply():
    assert multiply(3, 2) == 6
    assert multiply(-1, 1) == -1

def test_divide():
    assert divide(6, 2) == 3
    assert divide(-1, 1) == -1
