from .chip import Chip
from .Exceptions.invalid_operation_exception import InvalidOperationException
from .roll_dice_game import RollDiceGame
from .roll_dice_game import Dice


class Casino:

    def __init__(self, tables=1, chips_in_bank: Chip = Chip(0)):
        self._tables = tables
        self._free_table_count = tables * RollDiceGame.MAX_PLAYER_COUNT
        self._chips_in_bank = chips_in_bank

    def has_free_table(self):
        return self._free_table_count > 0

    def join_to_game(self, player):
        if self._free_table_count == 0:
            raise InvalidOperationException()
        dice = Dice()
        game = RollDiceGame(dice)
        player.join(game)
        self._free_table_count -= 1
        return game

    def sell(self, chips: Chip):
        self._chips_in_bank -= chips

    def has_chips(self, param):
        return self._chips_in_bank >= param

