from .Exceptions.invalid_operation_exception import InvalidOperationException
from .chip import Chip
from .i_roll_dice_game import IRollDiceGame


class Player:
    _current_game: IRollDiceGame = None
    _available_chips: Chip = Chip(0)

    def is_in_game(self) -> bool:
        return self._current_game is not None

    def join(self, game: IRollDiceGame):
        if self.is_in_game():
            raise InvalidOperationException()
        self._current_game = game
        self._current_game.add_player()

    def leave_game(self):
        if not self.is_in_game():
            raise InvalidOperationException()
        self._current_game.remove_player()
        self._current_game = None

    def buy(self, chips: Chip):
        self._available_chips = chips

    def has(self, chips: Chip) -> bool:
        return self._available_chips >= chips

    def take(self, chips: Chip):
        self._available_chips -= chips

    def win(self, chips: Chip):
        self._available_chips += chips
