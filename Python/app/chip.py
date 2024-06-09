from .Exceptions.invalid_operation_exception import InvalidOperationException


class Chip:
    _amount = 0

    def __init__(self, amount) -> None:
        self._amount = amount

    def __eq__(self, other):
        if not isinstance(other, Chip):
            raise InvalidOperationException()
        return self._amount == other._amount

    def __ge__(self, other):
        if not isinstance(other, Chip):
            raise InvalidOperationException()
        return self._amount >= other._amount

    def __le__(self, other):
        if not isinstance(other, Chip):
            raise InvalidOperationException()
        return self._amount <= other._amount

    def __add__(self, other):
        if not isinstance(other, Chip):
            raise InvalidOperationException()
        return Chip(self._amount + other._amount)

    def __sub__(self, other):
        if not isinstance(other, Chip):
            raise InvalidOperationException()
        return Chip(self._amount - other._amount)

    def __mul__(self, value):
        return Chip(self._amount * value)
