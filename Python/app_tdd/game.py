class Game:

    def __init__(self) -> None:
        self.min_player_number = 2
        self.players = []

    def players_enough_to_start_game(self):
        return len(self.players) >= self.min_player_number

    def get_players_number(self):
        return len(self.players)
    
    def add_player(self, player):
        self.players.append(player)