from app.chip import Chip

def test_pass():
    assert Chip(1) == Chip(1)

def test_fail():
    assert Chip(0) == Chip(1)
