from app import Chip, Player, RollDiceGame, Bet
from typing import Optional

class Create:
    lucky_score = 6
    class Player:
        def __init__(self, is_lucky=False, chips: Chip=Chip(10)) -> None:
            self._is_lucky = is_lucky
            self._player = Player()
            self._player.buy(chips)




        def bet(self, chips: Chip, score: Optional[int]):
            if self._is_lucky:
                score = lucky_score
            self.bet = Bet(chips, score)
            return self


    class Game:
        def __init__(self, player: Player) -> None:
            self._game = RollDiceGame()
            self._game.add_player(player)

        def add_player(self, player):
            self._game.add_player(player)
            return self
