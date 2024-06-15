from app.player import Player
from app.chips import Chips


class Casino:
    def sell(self, player: Player, chips: Chips):
        player.deposit(chips)
