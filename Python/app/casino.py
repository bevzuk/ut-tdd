from .Exceptions.invalid_operation_exception import InvalidOperationException
from .roll_dice_game import RollDiceGame
from .roll_dice_game import Dice


class Casino:

    def __init__(self, tables=1, seats_per_table=1):
        self._tables = tables
        self._seats_per_table = seats_per_table
        self._free_table_count = tables * seats_per_table

    def has_free_table(self):
        return True

    def join_to_game(self, player):
        if self._free_table_count == 0:
            raise InvalidOperationException()
        dice = Dice()
        game = RollDiceGame(dice)
        player.join(game)
        self._free_table_count -= 1
