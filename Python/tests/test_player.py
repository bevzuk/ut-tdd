class Player:
    def get_chips(self):
        return Chips(100)


class Casino:
    def sell(self, player, param):
        pass


class Chips:
    def __init__(self, amount: int):
        self._amount = amount

    def __eq__(self, other):
        return self._amount == other._amount


def test_player_can_buy_chips_in_casino():
    player = Player()
    casino = Casino()

    casino.sell(player, Chips(100))

    assert player.get_chips() == Chips(100)
