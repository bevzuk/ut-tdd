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

# @pytest.fixture
# def setup_game():


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

def test_can_win_with_gaining_chips(setup_player_with_5_chips_in_game):
    player, game = setup_player_with_5_chips_in_game
    dice = Dice()
    win_score = 1
    dice.roll = MagicMock(return_value = win_score)
    game.set_dice(dice)
    bet = Bet(Chip(5), win_score)
    game.bet(player, bet)

    game.play()

    assert player.has(Chip(5*6))

def test_can_loose_with_loosing_chips(setup_player_with_5_chips_in_game):
    player, game = setup_player_with_5_chips_in_game
    dice = Dice()
    win_score = 1
    dice.roll = MagicMock(return_value = win_score)
    game.set_dice(dice)
    bet = Bet(Chip(1), win_score * 2)
    game.bet(player, bet)

    game.play()

    assert player.has(Chip(4))
