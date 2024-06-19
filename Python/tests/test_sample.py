from app import *


def test_pass():
    assert Chip(1) == Chip(1)


def test_dice_range():
    assert Dice.roll() in range(1, 6)

def test_player_not_in_game():
    player = Player()
    assert player.is_in_game() is False

def test_player_join_to_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    assert player._current_game == game

def test_player_leave_game():
    player = Player()
    game = RollDiceGame()
    player.join(game)
    player.leave_game()
    assert player.is_in_game() is False


def test_player_buy_chips():
    pass
