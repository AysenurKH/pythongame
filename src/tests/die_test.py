"""Tests related to the die.py file."""

from src.die import Die


def test_constructor():
    """Tests the constructor and its parameters."""
    die1 = Die()
    assert die1.value is None
    die2 = Die(4)
    assert die2.value == 4


def test_roll():
    """Tests the roll() function."""
    die = Die()
    assert die.value is None
    value = die.roll()
    assert value == die.value
    assert 1 <= value <= 6


def test_str():
    """Tests the overridden __str__ function."""
    die = Die(4)
    assert str(die) == "⚃"
