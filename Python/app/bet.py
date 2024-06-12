from .chip import Chip


class Bet:
    chips: Chip
    face_value: int

    def __init__(self, chips: Chip, face_value: int) -> None:
        self.chips = chips
        self.face_value = face_value
