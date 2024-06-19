from app import *
import pytest
#from Python.app.Exceptions.invalid_operation_exception import InvalidOperationException


def test_chip_eq():
    assert Chip(1) == Chip(1)

# def test_chip_eq_badarg():
#     with pytest.raises(Exception):
#         Chip(1) == 31
        
def test_chip_ne():
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
    
    
    
    
    
