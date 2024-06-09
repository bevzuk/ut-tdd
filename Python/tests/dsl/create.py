from tests.dsl.game_builder import GameBuilder
from tests.dsl.player_builder import PlayerBuilder


class Create:
    @classmethod
    def game(cls) -> GameBuilder:
        return GameBuilder()

    @classmethod
    def player(cls) -> PlayerBuilder:
        return PlayerBuilder()
