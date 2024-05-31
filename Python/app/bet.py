from .chip import Chip


class Bet:
    chips = Chip(0)
    score = 0

    def __init__(self, chips: Chip, score: int) -> None:
        self.chips = chips
        self.score = score
