from .dsl import PlayerBuilder as Player


def test_can_join_game(game):
    player = Player().JoinGame(game)

    assert player.is_in_game()


def test_can_leave_game(game):
    player = Player().JoinGame(game)

    player.leave_game()

    assert player.is_in_game() is False



# def test_can_buy_chips(player):
#     # Player.BuyChips(10).HasChips(10)
#     player.buy(Chip(10))

#     assert (player.has(Chip(10)) is True)
#     assert (player.has(Chip(11)) is False)
