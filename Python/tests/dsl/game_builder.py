from unittest.mock import MagicMock

from app.roll_dice_game import RollDiceGame
from app.dice import Dice


class GameBuilder(RollDiceGame):
    lucky_face_value: int

    def __init__(self):
        self.lucky_face_value: int = 6
        self.dice = Dice()
        self.dice.roll = MagicMock(return_value=self.lucky_face_value)
        super().__init__(self.dice)

    def with_lucky_face_value(self, lucky_face_value: int):
        self.lucky_face_value = lucky_face_value
        self.dice.roll = MagicMock(return_value=self.lucky_face_value)
        return self
