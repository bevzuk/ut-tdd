import random

from .Exceptions.too_many_players_exception import TooManyPlayersException
from .bet import Bet
from .player import Player


class Dice:
    @staticmethod
    def roll():
        return random.randrange(1, 6)


class RollDiceGame:
    def __init__(self, dice: Dice):
        self._dice = dice
        self._players_count: int = 0
        self._bets = []

    def add_player(self):
        if self._players_count == 6:
            raise TooManyPlayersException()
        self._players_count += 1

    def remove_player(self):
        self._players_count -= 1

    def bet(self, player: Player, bet: Bet):
        self._bets.append({'player': player, 'chips': bet.chips, 'score': bet.score})
        player.take(bet.chips)

    def play(self):
        winning_score = self._dice.roll()
        for bet in self._bets:
            if bet['score'] == winning_score:
                bet['player'].win(bet['chips'] * 6)
