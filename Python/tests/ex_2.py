from app.player import Player
from app.roll_dice_game import RollDiceGame
from app.chip import Chip
from app.bet import Bet


def test_player_can_join_game():
    player = Player()
    game = RollDiceGame()

    player.join(game)
    assert player.is_in_game()


def test_player_can_buy_chips():
    player = Player()
    chip = Chip(2)
    player.buy(chip)
    assert player.has(Chip(2))


def test_player_can_make_bet():
    player = Player()
    player.buy(Chip(5))

    game = RollDiceGame()
    bet = Bet(Chip(5), 1)

    game.bet(player, bet)
    assert player.has(Chip(5)) is False


def test_player_can_leave_game():
    player = Player()
    game = RollDiceGame()

    player.join(game)
    player.leave_game()
    assert player.is_in_game() is False