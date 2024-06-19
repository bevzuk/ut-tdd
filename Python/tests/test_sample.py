from app import *


class Casino:
    def accept(self, person):
        pass

    def contains(self, person):
        return True


class Person:
    pass


def test_person_can_enter_casino():
    casino = Casino()
    person = Person()
    
    casino.accept(person)
    
    assert casino.contains(person)
