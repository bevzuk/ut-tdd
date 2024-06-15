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
