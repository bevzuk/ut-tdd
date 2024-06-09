from app.bet import Bet
from app.chip import Chip
from app.player import Player
from app.roll_dice_game import RollDiceGame


def test_player_by_default_has_no_chips():
    player = Player()
    assert player.has(Chip(0))


def test_player_can_buy_chips():
    player = Player()
    player.buy(Chip(1))
    assert player.has(Chip(1))


def test_player_can_make_bet():
    player = Player()
    player.buy(Chip(1))
    game = RollDiceGame()
    player.join(game)

    game.bet(player, Bet(Chip(1), 6))

    assert player.has(Chip(1)) is False
    assert player.has(Chip(0))


def test_player_by_default_not_in_game():
    player = Player()
    assert player.is_in_game() is False


def test_player_can_join_game():
    player = Player()

    player.join(RollDiceGame())

    assert player.is_in_game() is True


def test_player_can_leave_game():
    player = Player()
    player.join(RollDiceGame())

    player.leave_game()

    assert not player.is_in_game()


def test_player_can_loose():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    player.buy(Chip(10))
    game.bet(player, Bet(Chip(10), 1))

    game.play()

    assert not player.has(Chip(1))
