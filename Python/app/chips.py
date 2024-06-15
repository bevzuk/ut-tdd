class Chips:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount

    def __add__(self, other):
        return Chips(self._amount + other._amount)

    def __repr__(self):
        return f"{self._amount}"
