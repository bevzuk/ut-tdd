import pytest

from app.Exceptions.invalid_operation_exception import InvalidOperationException
from app.player import Player
from app.casino import Casino
from app.chips import Chips


def test_player_can_buy_chips_in_casino():
    player = Player()
    casino = Casino()

    casino.sell(player, Chips(100))

    assert player.get_chips() == Chips(100)


def test_player_can_buy_more_chips_in_casino():
    player = Player()
    casino = Casino()
    casino.sell(player, Chips(100))

    casino.sell(player, Chips(100))

    assert player.get_chips() == Chips(200)


def test_game_can_add_player():
    casino = Casino()
    player = Player()
    game = casino.get_open_game()

    game.add(player)

    assert player in casino.get_players_of(game)


def test_game_cant_add_player_second_time():
    casino = Casino()
    player = Player()
    game = casino.get_open_game()
    game.add(player)

    with pytest.raises(InvalidOperationException) as e:
        game.add(player)
        
    assert str(e.value) == "Player can't be added second time"


def test_two_games_can_not_add_same_player():
    casino = Casino()
    player = Player()
    game = casino.get_open_game()
    another_game = casino.get_open_game()
    casino.add(player, game)

    with pytest.raises(InvalidOperationException) as e:
        casino.add(player, another_game)

    assert str(e.value) == "Player should leave the game before joining another game"
