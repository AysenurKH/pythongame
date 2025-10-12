"""Tests related to the game.py file."""

from src.game import Game
from src.player import Player


def test_constructor():
    """Tests the constructor and its parameters."""
    player1 = Player("Aysenur")
    player2 = Player("Alice")
    game = Game(player1, player2, cheat=False)
    assert game.player1 == player1
    assert game.player2 == player2
    assert game.player1.name == "Aysenur"
    assert game.player2.name == "Alice"
    assert game.player1.dice_hand.get_value() == 0
    assert game.player2.dice_hand.get_value() == 0

    game = Game(player1, player2, cheat=True)
    assert game.player1.dice_hand.get_value() == 99


# Ths method writes data to the persisted high score file. Can't test it
def test_start_game_loop():
    """Tests the start_game_loop() function."""
    pass


# Ths method requires user input. Can't test it
def test_handle_player_turn():
    """Tests the handle_player_turn() function."""
    pass
