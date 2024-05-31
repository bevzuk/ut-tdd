from app.chip import Chip
from app.bet import Bet
from app.player import Player


def test_save_chips_amount():
    assert Chip(1).amount == 1


def test_save_bet_details():
    bet = Bet(Chip(1), 6)
    assert bet.chips.amount == 1
    assert bet.score == 6


def test_new_player_is_not_in_game():
    player = Player()
    assert not player.is_in_game()
