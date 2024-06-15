from app import Player, Casino
from app.chips import Chips


def test_player_can_buy_chips_in_casino():
    player = Player()
    casino = Casino()

    casino.sell(player, Chips(100))

    assert player.get_chips() == Chips(100)
