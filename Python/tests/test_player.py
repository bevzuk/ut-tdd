from unittest.mock import MagicMock

import pytest

from app import *


class PlayerContext:
    player: Player
    game: IRollDiceGame
    _score: int = 6

    def create_player(self):
        self.player = Player()
        return self

    def in_game(self):
        self.game = RollDiceGame()
        self.player.join(self.game)
        return self

    def with_chips(self, num_chips: int):
        self.player.buy(Chip(num_chips))
        return self

    def bets(self, num_chips: int):
        self.game.bet(self.player, Bet(Chip(num_chips), self._score))
        return self

    def wins(self):
        Dice.roll = MagicMock(return_value=self._score)
        return self

    def loses(self):
        Dice.roll = MagicMock(return_value=-1)
        return self


@pytest.fixture(scope='function')
def player():
    return Player()


@pytest.fixture(scope='function')
def game():
    return RollDiceGame()


@pytest.fixture(scope='function')
def player_in_game(player, game):
    player.join(game)
    return player, game


def test_is_not_in_game(player):
    assert player.is_in_game() is False


def test_can_join_game(player, game):
    player.join(game)

    assert player.is_in_game() is True


def test_can_buy_chips(player):
    player.buy(Chip(3))

    assert player.has(Chip(3))


def test_can_bet(player_in_game):
    player, game = player_in_game
    player.buy(Chip(3))

    game.bet(player, Bet(Chip(3), score=6))

    assert player.has(Chip(0))


def test_cannot_bet(player_in_game):
    player, game = player_in_game
    player.buy(Chip(3))

    with pytest.raises(InvalidOperationException):
        game.bet(player, Bet(Chip(5), score=6))


def test_can_leave_game(player_in_game):
    player, _ = player_in_game

    player.leave_game()

    assert player.is_in_game() is False


def test_can_win(player_in_game):
    player, game = player_in_game
    player.buy(Chip(3))
    game.bet(player, Bet(Chip(3), score=6))
    Dice.roll = MagicMock(return_value=6)

    game.play()

    assert player.has(Chip(3) * 6)


def test_can_lose(player_in_game):
    player, game = player_in_game
    player.buy(Chip(3))
    game.bet(player, Bet(Chip(3), score=6))
    Dice.roll = MagicMock(return_value=5)

    game.play()

    assert player.has(Chip(0))


def test_can_win_dsl():
    ctx = PlayerContext().create_player().in_game().with_chips(3).bets(3).wins()

    ctx.game.play()

    assert ctx.player.has(Chip(3) * 6)


def test_can_lose_dsl():
    ctx = PlayerContext().create_player().in_game().with_chips(3).bets(3).loses()

    ctx.game.play()

    assert ctx.player.has(Chip(0))
