from app import Chip
from app.Exceptions.invalid_operation_exception import InvalidOperationException

import pytest


class TestChip:
    def test_eq():
        assert Chip(1) == Chip(1)

    def test_ge():
        assert Chip(2) >= Chip(1)

    def test_ge_eq():
        assert Chip(2) >= Chip(2)

    def test_le():
        assert Chip(1) <= Chip(2)

    def test_le_eq():
        assert Chip(2) <= Chip(2)

    def test_exception_eq():
        with pytest.raises(InvalidOperationException):
            Chip(1) == 1

    def test_exception_le():
        with pytest.raises(InvalidOperationException):
            Chip(1) <= 1

    def test_exception_ge():
        with pytest.raises(InvalidOperationException):
            Chip(1) >= 1

    def test_exception_add():
        with pytest.raises(InvalidOperationException):
            Chip(1) + 1

    def test_exception_sub():
        with pytest.raises(InvalidOperationException):
            Chip(1) - 1

    def test_add():
        assert Chip(1) + Chip(1) == Chip(2)

    def test_sub():
        assert Chip(2) - Chip(1) == Chip(1)

    def test_mul():
        assert Chip(1) * 2 == Chip(2)
