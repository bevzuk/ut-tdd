from typing import List

from .Exceptions.too_many_players_exception import TooManyPlayersException
from .dice import Dice
from .player import Player
from .bet import Bet


class RollDiceGame:
    _players_count: int
    _bets: List

    def __init__(self, dice: Dice):
        self._dice = dice
        self._players_count = 0
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
