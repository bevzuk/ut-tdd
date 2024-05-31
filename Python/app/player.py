from .bet import Bet
from .chip import Chip
from .roll_dice_game import RollDiceGame


class Player:
    _current_game: RollDiceGame = None
    _available_chips: Chip = Chip(0)

    def is_in_game(self) -> bool:
        return self._current_game is not None

    def join(self, game: RollDiceGame):
        if self.is_in_game():
            return
            # throw new InvalidOperationException();
        self._current_game = game
        self._current_game.add_player()

    def leave_game(self):
        if not self.is_in_game():
            return
            # throw new InvalidOperationException();
        self._current_game.remove_player()
        self._current_game = None

    def buy(self, chips: Chip):
        self._available_chips = chips

    def has(self, chips: Chip) -> bool:
        return self._available_chips.amount >= chips.amount

    def bet(self, bet: Bet):
        pass
