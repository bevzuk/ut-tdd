from typing import Optional


class Gun:
    def __init__(self):
        self._num_bullet = 5

    def num_bullets(self):
        return self._num_bullet

    def charge_gun(self, num_bullet):
        self._num_bullet = num_bullet


class Game:
    def __init__(self) -> None:
        self._gun = None
        self._persons = []

    def get_gun(self) -> Optional[Gun]:
        return self._gun

    def get_num_persons(self) -> int:
        return 0


def test_gun_contains_5_bullets_by_default():
    gun = Gun()
    assert gun.num_bullets() == 5


def test_when_charged_gun_with_6_bullets_it_contain_exactly_6():
    gun = Gun()
    gun.charge_gun(num_bullet=6)
    assert gun.num_bullets() == 6


def test_default_game_does_not_contain_persons_and_guns():
    game = Game()

    assert game.get_num_persons() == 0
    assert game.get_gun() is None
