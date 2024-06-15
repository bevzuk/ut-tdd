class Chips:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount
