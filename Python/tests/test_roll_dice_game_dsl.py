from app import *

class bet_ex(Bet):
    def __init__(self, chips, score):
        super.__init__(Chip(chips), score)



class player_ext(Player):
    def buys(self, chips_nmb):
        chip = Chip(chips_nmb)
        return chip


class Create():
    def __init__(self):
        self.player = self.player = Player()

    def player(self):
        self.player = Player()
        self.player.with_10_chips = self.with_10_chips


def test_win_6_chips_dsl(setup_player_in_game):
    Create.player.buys(10).Chips().Bet(5)
    # Create player with 100 chips bets 5 chips wins x6
    Create.player.With
