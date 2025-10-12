"""Tests related to the dice_hand.py file."""

from src.dice_hand import DiceHand
from src.die import Die


def test_constructor():
    """Tests the constructor and its parameters."""
    dice_hand = DiceHand()
    assert not dice_hand.dice


def test_add_die():
    """Tests the add_die() function."""
    dice_hand = DiceHand()
    die1 = Die()
    dice_hand.add_die(die1)
    assert dice_hand.dice == [die1]
    die2 = Die(4)
    dice_hand.add_die(die2)
    assert dice_hand.dice == [die1, die2]
    assert dice_hand.dice[1].value == 4


def test_get_value():
    """Tests the get_value() function."""
    dice_hand = DiceHand()
    die1 = Die(3)
    die2 = Die(4)
    dice_hand.add_die(die1)
    dice_hand.add_die(die2)
    assert dice_hand.get_value() == 7


def test_str():
    """Tests the overridden __str__() function."""
    dice_hand = DiceHand()
    die1 = Die(3)
    die2 = Die(4)
    dice_hand.add_die(die1)
    dice_hand.add_die(die2)
    assert str(dice_hand) == "⚂ ⚃"


def test_clear():
    """Tests the clear() function."""
    dice_hand = DiceHand()
    die1 = Die(3)
    die2 = Die(4)
    dice_hand.add_die(die1)
    dice_hand.add_die(die2)
    dice_hand.clear()
    assert len(dice_hand.dice) == 0
    assert not dice_hand.dice
