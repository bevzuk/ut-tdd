from .chip import Chip


class Bet:
    def __init__(self, chips: Chip, score: int) -> None:
        self.chips = chips
        self.score = score
