from Python.app import *


def test_chip_add():
    assert Chip(1) + Chip(3) == Chip(4)


def test_chip_ge():
    assert Chip(4) >= Chip(1)


def test_chip_le():
    assert Chip(1) <= Chip(4)


def test_chip_sub():
    assert Chip(4) - Chip(1) == Chip(3)


def test_chip_mul():
    assert Chip(1) * 4 == Chip(4)


