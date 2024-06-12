from unittest.mock import MagicMock

from app.roll_dice_game import RollDiceGame
from app.dice import Dice


class GameBuilder(RollDiceGame):
    lucky_score: int

    def __init__(self):
        self.lucky_score: int = 6
        self.dice = Dice()
        self.dice.roll = MagicMock(return_value=self.lucky_score)
        super().__init__(self.dice)

    def with_lucky_score(self, lucky_score: int):
        self.lucky_score = lucky_score
        self.dice.roll = MagicMock(return_value=self.lucky_score)
        return self
