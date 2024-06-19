from Python.app import *


class FakeDice(IDice):
    @staticmethod
    def roll():
        return 5


def test_player_wins():
    game = RollDiceGame(FakeDice())
    lucky_player = Player()
    lucky_player.join(game)
    lucky_player.buy(Chip(4))

    game.bet(lucky_player, Bet(Chip(4), 5))
    game.play()

    assert lucky_player.has(Chip(4) * 6), "Game plays wrong"


def test_player_lose():
    game = RollDiceGame(FakeDice())
    lucky_player = Player()
    lucky_player.join(game)
    lucky_player.buy(Chip(4))

    game.bet(lucky_player, Bet(Chip(4), 4))
    game.play()

    assert lucky_player.has(Chip(0)), "Game plays wrong"


def test_plays_correctly_with_mock(mocker):
    mocked_dice = mocker.patch('Python.app.dice.Dice.roll', FakeDice)

    game = RollDiceGame(mocked_dice)
    lucky_player = Player()
    lucky_player.join(game)
    lucky_player.buy(Chip(4))

    game.bet(lucky_player, Bet(Chip(4), 5))

    game.play()

    assert lucky_player.has(Chip(4) * 6), "Game plays wrong"
