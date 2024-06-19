from app import Chip
from app.Exceptions.invalid_operation_exception import InvalidOperationException

import pytest


class TestChip:
    def test_eq(self):
        assert Chip(1) == Chip(1)

    def test_ge(self):
        assert Chip(2) >= Chip(1)

    def test_ge_eq(self):
        assert Chip(2) >= Chip(2)

    def test_le(self):
        assert Chip(1) <= Chip(2)

    def test_le_eq(self):
        assert Chip(2) <= Chip(2)

    def test_exception_eq(self):
        with pytest.raises(InvalidOperationException):
            Chip(1) == 1

    def test_exception_le(self):
        with pytest.raises(InvalidOperationException):
            Chip(1) <= 1

    def test_exception_ge(self):
        with pytest.raises(InvalidOperationException):
            Chip(1) >= 1

    def test_exception_add(self):
        with pytest.raises(InvalidOperationException):
            Chip(1) + 1

    def test_exception_sub(self):
        with pytest.raises(InvalidOperationException):
            Chip(1) - 1

    def test_add(self):
        assert Chip(1) + Chip(1) == Chip(2)

    def test_sub(self):
        assert Chip(2) - Chip(1) == Chip(1)

    def test_mul(self):
        assert Chip(1) * 2 == Chip(2)
