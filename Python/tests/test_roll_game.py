from typing import List
from unittest.mock import MagicMock
from app import *
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "/Python")
from app.Exceptions.invalid_operation_exception import InvalidOperationException
#from app.Exceptions.too_many_player_exception import TooManyPlayersException


@pytest.fixture
def setup_player_and_game():
    player = Player()
    game = RollDiceGame()
    return  player, game


@pytest.fixture
def setup_game_with_player_with_2_chips_and_dice_mock_1_score():
    player = Player()
    dice = Dice()
    dice.roll = MagicMock(return_value = 1)
    bet = Bet(Chip(2), 1)
    game = RollDiceGame(dice)
    player.buy(Chip(2))
    player.join(game)
    game.bet(player, bet)
    return  player, game


def test_roll_game_default_values(setup_player_and_game):
    player, game = setup_player_and_game
    player.join(game)
    with pytest.raises(InvalidOperationException):
        game.bet(player, Bet(Chip(1), 2))
    
    
def test_player_win_game(setup_game_with_player_with_2_chips_and_dice_mock_1_score):
    player, game = setup_game_with_player_with_2_chips_and_dice_mock_1_score

    game.play()
    
    assert player.has(Chip(12))

class DSL:
    _game: RollDiceGame
    _dice: Dice
    _player: Player
    _bet: Bet
    _chips: Chip
    
    def __init__(self):
        
        self._game = None
        self._player = None
        self._bet = None
        self._chips = None
        self._win_flag = None
    
    def create_win_game(self):
        self._win_flag = True
        dice = Dice()
        dice.roll = MagicMock(return_value = 1)
        self._game = RollDiceGame(dice)
        return self

    def create_loose_game(self):
        self._win_flag = False
        dice = Dice()
        dice.roll = MagicMock(return_value = 2)
        self._game = RollDiceGame(dice)
        return self
    
    def with_player(self):
        self._player = Player()
        self._player.join(self._game)
        return self
    
    def with_chips(self, chips):
        self._chips=chips
        self._player.buy(chips)
        return self
    
    def with_allin_bet(self):
        self._bet = Bet(self._chips, 1)
        self._game.bet(self._player, self._bet)
        return self
    
    def get_game_and_player(self):
        return self._game, self._player
    

def test_player_win_game_dsl():
    start_chips = 2
    chips_after_win = start_chips*6 # six bet, when win
    dsl = DSL().create_win_game().with_player().with_chips(Chip(start_chips)).with_allin_bet()
    game, player = dsl.get_game_and_player()
    
    game.play()
    assert player.has(Chip(chips_after_win))
    