"""Tests related to the player.py file."""

from src.player import Player
from src.intelligence import Intelligence
from src.die import Die


def test_constructor():
    """Tests the constructor and its parameters."""
    player = Player("Aysenur")
    assert not isinstance(player, Intelligence)
    assert player.name == "Aysenur"
    assert player.score == 0
    assert player.dice_hand.get_value() == 0


def test_set_name():
    """Tests the set_name() function."""
    player = Player("Aysenur")
    player.set_name("Alice")
    assert player.name == "Alice"


def test_get_score_increment_score():
    """Tests the get_score() and increment_score() functions."""
    player = Player("Aysenur")
    assert player.get_score() == 0
    player.increment_score(5)
    assert player.get_score() == 5


# Requires user input. Cannot be tested
def test_get_roll_dice_choice():
    """Tests the get_roll_dice_choice() function."""
    pass


def test_empty_dice_hand():
    """Tests the empty_dice_hand() function."""
    player = Player("Aysenur")
    player.dice_hand.add_die(Die(4))
    assert player.dice_hand.dice[0].value == 4
    assert len(player.dice_hand.dice) == 1
    assert player.dice_hand.get_value() == 4
    player.empty_dice_hand()
    assert not player.dice_hand.dice
    assert player.dice_hand.get_value() == 0


def test_reset():
    """Tests the reset() function."""
    player = Player("Aysenur")
    player.dice_hand.add_die(Die(4))
    player.score = 25
    assert player.dice_hand.dice[0].value == 4
    assert len(player.dice_hand.dice) == 1
    assert player.dice_hand.get_value() == 4
    assert player.score == 25
    player.reset()
    assert not player.dice_hand.dice
    assert player.dice_hand.get_value() == 0
    assert player.score == 0
