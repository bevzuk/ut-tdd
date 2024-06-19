from app import *


class PlayerBuilder:
    def __init__(self):
        self._player = Player()

    def JoinGame(self, game):
        self._player.join(game)
        return self

    def LeaveGame(self):
        self._player.leave_game()
        return self

    def __getattr__(self, name):
        def wrapper(*args, **kwargs):
            return getattr(self._player, name)(*args, **kwargs)
        return wrapper
