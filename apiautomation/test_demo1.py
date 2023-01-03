import pytest


def test_m1():
    a = 5
    b = 6
    assert a == b, "not equal"


def test_m2():
    name="python"
    assert name.upper() == "PYTHON", "yes they are equal"
