from .dsl import PlayerBuilder as Player


def test_can_join_game(game):
    assert Player().JoinGame(game).is_in_game()


def test_can_leave_game(game):
    assert Player().JoinGame(game).LeaveGame().is_in_game() is False



# def test_can_buy_chips(player):
#     # Player.BuyChips(10).HasChips(10)
#     player.buy(Chip(10))

#     assert (player.has(Chip(10)) is True)
#     assert (player.has(Chip(11)) is False)
