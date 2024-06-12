from .chip import Chip


class Bet:
    chips: Chip
    score: int

    def __init__(self, chips: Chip, score: int) -> None:
        self.chips = chips
        self.score = score
