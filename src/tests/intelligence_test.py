"""Tests related to the intelligence.py file."""

from src.intelligence import Intelligence
from src.player import Player

# These tests are not good. It's not possible to test random behavior, so it is limited what I can test.
# I would have preferred if could test that the computer with difficulty 1 would pick the roll_dice_easy() function, etc


def test_constructor():
    """Tests the constructor and its parameters."""
    intelligence = Intelligence(1)
    assert issubclass(type(intelligence), Player)
    assert intelligence.computer_difficulty == 1
    assert intelligence.name == "Computer"
    assert intelligence.score == 0
    assert intelligence.dice_hand.get_value() == 0


def test_get_roll_dice_choice():
    """Tests the get_roll_dice_choice() function."""
    opponent = Player("Opponent")
    intelligence = Intelligence(1)
    assert intelligence.get_roll_dice_choice() in {"y", "n"}
    intelligence = Intelligence(2)
    assert intelligence.get_roll_dice_choice() in {"y", "n"}
    intelligence = Intelligence(3)
    assert intelligence.get_roll_dice_choice(opponent) in {"y", "n"}


# The computer has no dice at the moment. It will always choose to roll the die
def test_roll_dice_easy():
    """Tests the roll_dice_easy() function."""
    intelligence = Intelligence(1)
    assert intelligence.roll_dice_easy() == "y"


# The computer has no dice at the moment. It will always choose to roll the die
def test_roll_dice_medium():
    """Tests the roll_dice_medium() function."""
    intelligence = Intelligence(2)
    assert intelligence.roll_dice_medium() == "y"


# Hard difficulty will always choose to roll if score is above or equal to 71
def test_roll_dice_hard():
    """Tests the roll_dice_hard() function."""
    opponent = Player("Opponent")
    intelligence = Intelligence(3)
    intelligence.score = 71
    assert intelligence.roll_dice_hard(opponent) == "y"
