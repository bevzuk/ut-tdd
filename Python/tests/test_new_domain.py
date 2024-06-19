import random
from unittest.mock import MagicMock


class KillingPlace:
    def __init__(self):
        self.human_count = 0
        # self.patron_count = 1
        self.baraban = [0, 0, 1, 0, 0, 0]

    def addParticipians(self):
        self.human_count = 2

    def trigger_revolver(self):
        return self.baraban[random.randrange(1, 6)]

    def shoot(self):
        if self.trigger_revolver():
            self.human_count = 1


def test_human_can_join_KillingPlace():
    killingPlace = KillingPlace()
    killingPlace.addParticipians()
    assert killingPlace.human_count == 2


def test_human_shoot_success_KillingPlace():
    killingPlace = KillingPlace()
    killingPlace.addParticipians()

    killingPlace.trigger_revolver = MagicMock(return_value=True)

    killingPlace.shoot()
    assert killingPlace.human_count == 1


def test_human_shoot_fail_KillingPlace():
    killingPlace = KillingPlace()
    killingPlace.addParticipians()

    killingPlace.trigger_revolver = MagicMock(return_value=False)

    killingPlace.shoot()
    assert killingPlace.human_count == 2
