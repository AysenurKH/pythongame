from src.die import Die


def test_constructor():
    die1 = Die()
    assert die1.value is None
    die2 = Die(4)
    assert die2.value == 4


def test_roll():
    die = Die()
    assert die.value is None
    value = die.roll()
    assert value == die.value
    assert 1 <= value <= 6


def test_str():
    die = Die(4)
    assert str(die) == "⚃"
