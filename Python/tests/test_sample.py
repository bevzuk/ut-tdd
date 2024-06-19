from app.Casino import Casino
from app.Person import Person


def test_person_can_enter_casino():
    casino = Casino()
    person = Person()

    casino.accept(person)

    assert casino.contains(person)


def test_casino_person_count_1_when_single_person_is_accepted():
    casino = Casino()
    person = Person()

    casino.accept(person)

    assert casino.get_persons_count() == 1


def test_casino_has_no_persons_by_default():
    casino = Casino()

    assert casino.get_persons_count() == 0
