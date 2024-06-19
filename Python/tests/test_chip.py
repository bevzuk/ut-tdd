from app import *
import pytest

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/Python")
from app.Exceptions.invalid_operation_exception import InvalidOperationException


def test_chip_equal():
    assert Chip(1) == Chip(1)
        
def test_chip_not_equal():
    assert Chip(1) != Chip(2)
    
    
def test_chip_ge():
    assert Chip(2) >= Chip(1)


def test_chip_le():
    assert Chip(1) <= Chip(2)
    
    
def test_chip_sum():
    assert Chip(1) + Chip(1) == Chip(2)
    
    
def test_chip_sub():
    assert Chip(2) - Chip(1) == Chip(1)
    

def test_chip_mul():
    assert Chip(2) * 2 == Chip(4)
    
def test_chip_eq_badarg():
    with pytest.raises(InvalidOperationException):
        Chip(1) == 31    
    
def test_chip_ne_badarg():
    with pytest.raises(InvalidOperationException):
        Chip(1) != 31    
        
def test_chip_le_badarg():
    with pytest.raises(InvalidOperationException):
        Chip(1) <= 31    
        
def test_chip_ge_badarg():
    with pytest.raises(InvalidOperationException):
        Chip(1) >= 31    
    
def test_chip_sub_badarg():
    with pytest.raises(InvalidOperationException):
        some_chip = Chip(1) - 31    
    
def test_chip_add_badarg():
    with pytest.raises(InvalidOperationException):
        some_chip = Chip(1) + 31    
    

