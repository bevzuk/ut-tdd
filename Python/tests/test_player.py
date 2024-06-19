import pytest
from app.roll_dice_game import RollDiceGame
from app.Exceptions.too_many_players_exception import TooManyPlayersException
from app.player import Player
from app.chip import Chip
from app.bet import Bet



def test_new_player_has_no_chips():
    player = Player()
    assert player.has(Chip(0))

def test_player_can_buy_chips():
    player = Player()
    chips = Chip(5)
    player.buy(chips)
    assert player.has(Chip(5))

def test_player_can_bet():
    player = Player()
    game = RollDiceGame()
    game.add_player()
    chips = Chip(5)

    player.buy(chips)
    bet = Bet(chips, 1)
    game.bet(player, bet)

    assert True



