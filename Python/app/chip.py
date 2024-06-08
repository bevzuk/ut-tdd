class Chip:
    amount = 0

    def __init__(self, amount) -> None:
        self.amount = amount

    def __ge__(self, other):
        return self.amount >= other.amount

    def __le__(self, other):
        return self.amount <= other.amount
