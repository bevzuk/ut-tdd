from app.chip import Chip


def test_eq():
    assert Chip(1) == Chip(1)

def test_add():
    chip_1 = Chip(2)
    chip_2 = Chip(3)
    chip_res = chip_1 + chip_2
    assert chip_res == Chip(5)

def test_ge():
    chip_1 = Chip(2)
    chip_2 = Chip(3)
    assert chip_2 >= chip_1

def test_le():
    chip_1 = Chip(2)
    chip_2 = Chip(3)
    assert chip_1 <= chip_2

def test_ge_eq():
    chip_1 = Chip(2)
    chip_2 = Chip(2)
    assert chip_2 >= chip_1

def test_le_eq():
    chip_1 = Chip(2)
    chip_2 = Chip(2)
    assert chip_1 <= chip_2

def test_sub():
    chip_1 = Chip(2)
    chip_2 = Chip(3)
    chip_res = chip_2 - chip_1
    assert chip_res == Chip(1)

## devs, is that expected?
def test_sub_negative():
    chip_1 = Chip(2)
    chip_2 = Chip(3)
    chip_res = chip_1 - chip_2
    assert chip_res == Chip(-1)

def test_mul():
    chip = Chip(2)
    chip_res = chip * 3
    assert chip_res == Chip(6)
