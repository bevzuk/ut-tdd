from app.bet import Bet
from app.chip import Chip
from app.player import Player
from tests.dsl.game_builder import GameBuilder


class PlayerBuilder(Player):
    def __init__(self):
        super().__init__()
        self._game: GameBuilder() = None
        self._lucky = False

    def lucky_in(self, game: GameBuilder):
        self._lucky = True
        self._game = game
        self.join(game)
        return self

    def unlucky_in(self, game: GameBuilder):
        self._lucky = False
        self._game = game
        self.join(game)
        return self

    def with_bet(self, chips_amount: int):
        if not self.has(Chip(chips_amount)):
            self.buy(Chip(chips_amount))
        self._game.bet(self, Bet(Chip(chips_amount), self._get_score()))
        return self

    def with_chips(self, chips_amount: int):
        self.buy(Chip(chips_amount))
        return self

    def _get_score(self):
        if self._lucky:
            return self._game.lucky_score
        else:
            return self._game.lucky_score + 1
