from .Exceptions.too_many_players_exception import TooManyPlayersException


class RollDiceGame:
    players_count: int = 0

    def add_player(self):
        if self.players_count == 6:
            raise TooManyPlayersException()
        self.players_count += 1

    def remove_player(self):
        self.players_count -= 1
