
from app import *
import pytest

def chip_eq():
    assert Chip(1) == Chip(1)

def chip_eq():
    with pytest.raises (InvalidOperationException()):
        Chip(1) == 32

def test_bet():
    