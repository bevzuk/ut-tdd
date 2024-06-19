import pathlib
import sys

import pytest

from app import *

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from app.Exceptions.invalid_operation_exception import InvalidOperationException


def test_eq_1_1_pass():
    assert Chip(1) == Chip(1)

def test_eq_2_1_pass():
    assert Chip(2) == Chip(1)

@pytest.mark.parametrize("chip_1, chip_2", [(2, 1), (2, 2)])
def test_ge_pass(chip_1, chip_2):
    assert Chip(chip_1) >= Chip(chip_2)

def test_ge_1_2_pass():
    assert not (Chip(1) >= Chip(2))

def test_eq_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) == list()

def test_ge_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) >= list()

def test_le_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) <= list()

def test_add_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) + list()

def test_sub_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) - list()

def test_sub_ex():
    with pytest.raises(InvalidOperationException):
        Chip(1) - list()

