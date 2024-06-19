from app import *
from app.Exceptions.invalid_operation_exception import InvalidOperationException
import pytest

class TestDice:
    def test_should_roll_less_than_6(self):
        assert Dice.roll() <= 6

    def test_should_roll_greater_than_1(self):
        assert Dice.roll() >= 1


class TestBet:
    def test_can_init(self):
        bet = Bet(Chip(1), 1)

        assert bet.chips == Chip(1)
        assert bet.score == 1


class TestChip:
    def test_pass(self):
        assert Chip(1) == Chip(1)

    @pytest.mark.skip('Invalid code, should be fixed')
    def test_cant_assign_negative(self):
        with self.assertRaises(BaseException):
            Chip(-1)

    def test_greater_chips_are_greater(self):
        chip1 = Chip(1)
        chip2 = Chip(2)

        assert chip2 >= chip1

    def test_smaller_chips_are_smaller(self):
        chip1 = Chip(1)
        chip2 = Chip(2)

        assert chip1 <= chip2

    def test_can_add_another_chip(self):
        chip1 = Chip(1)
        chip2 = Chip(2)

        chip_sum = chip1 + chip2

        assert chip_sum == Chip(3)

    def test_can_sub_smaller_chip(self):
        chip1 = Chip(11)
        chip2 = Chip(29)

        chip_sub = chip2 - chip1

        assert chip_sub == Chip(18)

    @pytest.mark.skip('Invalid code, should be fixed')
    def test_cant_sub_greater_chip(self):
        chip1 = Chip(11)
        chip2 = Chip(29)

        with self.assertRaises(BaseException):
            chip1 - chip2

    def test_can_mul_value(self):
        chip1 = Chip(9945)

        chip_mul = chip1 * 198

        assert chip_mul == Chip(1969110)


class TestPlayer:
    @pytest.fixture
    @staticmethod
    def setup_player_in_game():
        game = RollDiceGame()
        player = Player()
        player.join(game)

        return (player, game)

    def test_can_init(self):
        player = Player()

        assert isinstance(player, Player)

    def test_init_with_zero_chips(self):
        assert Player().has(Chip(0))
        assert Player().has(Chip(1)) is False

    def test_can_join_to_game(self):
        game = RollDiceGame()
        player = Player()

        try:
            player.join(game)
        except BaseException as e:
            pytest.fail(str(e))

    def test_cannot_join_to_game_twice(self, setup_player_in_game):
        player, game = setup_player_in_game

        with pytest.raises(InvalidOperationException):
            player.join(game)

    def test_can_buy_chips(self, setup_player_in_game):
        player, _ = setup_player_in_game

        player.buy(Chip(10))

        assert player.has(Chip(10))
        assert not player.has(Chip(11))
