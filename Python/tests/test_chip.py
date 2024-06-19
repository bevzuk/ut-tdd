from app import *


def test_chip_equals():
    assert Chip(1) == Chip(1)

def test_chip_mul():
    assert Chip(1) * 3 == Chip(3)

def test_chip_sub():
    assert Chip(3) - Chip(2) == Chip(1)

def test_chip_add():
    assert Chip(1) + Chip(2) == Chip(3)

def test_chip_greater():
    assert Chip(3) >= Chip(1)

def test_chip_greater_or_equals():
    assert Chip(3) >= Chip(3)

def test_chip_less():
    assert Chip(1) <= Chip(3)

def test_chip_less_or_equals():
    assert Chip(3) <= Chip(3)
