from sci_calc import *


def test_find_sqrt():
    assert find_sqrt(100) == 10.0


def test_find_ceil():
    assert find_ceil(12.7) == 13
    assert find_ceil(120.2) == 121


def test_division():
    assert division(20, 5) == 4
