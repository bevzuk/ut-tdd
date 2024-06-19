from Python.app import *


def test_pass():
    assert Chip(1) == Chip(1)


def test_full_game():
    game = RollDiceGame(Dice())

    victor = Player()
    vladimir = Player()

    victor.join(game)
    vladimir.join(game)

    victor.buy(Chip(10))
    vladimir.buy(Chip(10))

    game.bet(victor, Bet(Chip(10), 5))
    game.bet(vladimir, Bet(Chip(10), 3))

    game.play()

    if victor.has(Chip(60)):
        print('VICTOR WIN !')
    elif vladimir.has(Chip(60)):
        print('VLADIMIR WIN !')
    else:
        print('VICTOR & VLADIMIR LOSE !')

