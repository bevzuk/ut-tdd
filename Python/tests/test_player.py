import pytest
from app.roll_dice_game import RollDiceGame
from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.Exceptions.too_many_players_exception import TooManyPlayersException
from app.player import Player
from app.chip import Chip
from app.bet import Bet
from app.dice import Dice
from unittest.mock import MagicMock

@pytest.fixture
def setup_player_with_5_chips_in_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    chips = Chip(5)
    player.buy(chips)

    return player, game

class Create:
    def __init__(self):
        self._player = None
        self._dice = None
        self._game = None

    def make_dice(self, is_cheater=True):
        self._dice = Dice()
        win_score = 1
        self._dice.roll = MagicMock(return_value = win_score)
        return self

    def player(self, is_cheater=True):
        self._player = Player()
        self.make_dice(is_cheater)
        return self

    def buys_chips(self, n_chips=5):
        chips = Chip(n_chips)
        self._player.buy(chips)
        return self

    def joins_game(self):
        self._game = RollDiceGame(self._dice)
        self._player.join(self._game)
        return self

    def bets_chips(self, n_chips = 1, win_score = 1):
        bet = Bet(Chip(n_chips), win_score)
        self._game.bet(self._player, bet)
        return self

    def gains(self, n_chips):
        self._game.play()

        assert self._player.has(Chip(n_chips))



def test_has_no_chips_by_default():
    player = Player()
    assert player.has(Chip(0))

def test_can_buy_chips(setup_player_with_5_chips_in_game):
    player, _ = setup_player_with_5_chips_in_game
    assert player.has(Chip(5))

def test_spend_chips_on_betting_in_game(setup_player_with_5_chips_in_game):
    player, game = setup_player_with_5_chips_in_game
    bet = Bet(Chip(2), 1)

    game.bet(player, bet)

    assert player.has(Chip(3))
    assert not player.has(Chip(4))

def test_when_not_enough_chips_cannot_bet(setup_player_with_5_chips_in_game):
    player, game = setup_player_with_5_chips_in_game
    bet = Bet(Chip(10), 3)

    with pytest.raises(InvalidOperationException):
        game.bet(player, bet)

def test_can_win_with_gaining_chips_dsl():
    Create().player(is_cheater=True).buys_chips(n_chips=5).joins_game().bets_chips(n_chips=1).gains(n_chips=5 - 1 + 1 * 6)
 