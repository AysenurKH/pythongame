"""Tests related to the high_score.py file."""

from src.high_score import HighScore
from src import high_score
from src.player import Player


def test_constructor():
    """Tests the constructor and its parameters."""
    hs = HighScore("Aysenur", 4, 3)
    assert hs.name == "Aysenur"
    assert hs.games_played == 4
    assert hs.games_won == 3


def test_increment_games_won():
    """Tests the increment_games_won() function."""
    hs = HighScore("Aysenur", 4, 3)
    hs.increment_games_won()
    assert hs.games_played == 4
    assert hs.games_won == 4


def test_increment_games_played():
    """Tests the increment_games_played() function."""
    hs = HighScore("Aysenur", 4, 3)
    hs.increment_games_played()
    assert hs.games_played == 5
    assert hs.games_won == 3


def test_str():
    """Tests the overriden __str__() function."""
    hs = HighScore("Aysenur", 4, 3)
    assert str(hs) == "Aysenur 4 3"


def test_from_persisted_line():
    """Tests the from_persisted_line() function."""
    hs = high_score.from_persisted_line("Aysenur 4 3")
    assert isinstance(hs, HighScore)
    assert hs.name == "Aysenur"
    assert hs.games_played == 4
    assert hs.games_won == 3


# Probably a bad test. The high score file could contain anything, and running the test multiple times causes the file
# to look different ever time.
def test_persistence():
    """Tests the persist_win() and get_high_score functions."""
    player1 = Player("Aysenur")
    player2 = Player("Alice")
    high_score.persist_win(player1, player2)
    high_scores = high_score.get_high_scores()
    assert high_scores[player1.name].name == "Aysenur"
    assert high_scores[player1.name].games_played >= 1
    assert high_scores[player1.name].games_won >= 1
    assert high_scores[player2.name].name == "Alice"
    assert high_scores[player2.name].games_played >= 1
    assert high_scores[player2.name].games_won >= 0
