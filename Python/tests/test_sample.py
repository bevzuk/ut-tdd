from app.Casino import Casino
from app.Person import Person


def test_person_can_enter_casino():
    casino = Casino()
    person = Person()

    casino.accept(person)

    assert casino.contains(person)


def test_casino_can_accept_two_persons():
    casino = Casino()
    person1 = Person()
    person2 = Person()

    casino.accept(person1)
    casino.accept(person2)

    assert casino.get_persons_count() == 2


def test_casino_person_count_1_when_single_person_is_accepted():
    casino = Casino()
    person = Person()

    casino.accept(person)

    assert casino.get_persons_count() == 1


def test_casino_has_no_persons_by_default():
    casino = Casino()

    assert casino.get_persons_count() == 0


def test_when_casino_kick_out_person_she_is_not_in_casino_anymore():
    casino = Casino()
    person = Person()
    casino.accept(person)

    casino.kickout(person)

    assert not casino.contains(person)

