import random

from .bet import Bet
from .player import Player
from .Exceptions.too_many_players_exception import TooManyPlayersException


class RollDiceGame:
    _players_count: int = 0
    _bets = []

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
        winning_score = random.randrange(1, 6)
        for bet in self._bets:
            if bet['score'] == winning_score:
                bet['player'].win(bet['chips'] * 6)
