from app import Player, Chip


def assert_player_has_chips(player: Player, chips_amount: int):
    assert player.has(Chip(chips_amount))
    assert not player.has(Chip(chips_amount + 1))
