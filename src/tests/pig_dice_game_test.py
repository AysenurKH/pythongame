"""Tests related to the pig_dice_game.py file."""

from cmd import Cmd
from src.pig_dice_game import CommandListener


def test_constructor():
    """Tests the constructor and its parameters."""
    cmd = CommandListener()
    assert issubclass(type(cmd), Cmd)


# Can't test because it requires player input
def test_do_play():
    """Tests the do_play() function."""
    pass


# Doesn't return anything, can't test
def test_rules():
    """Tests the do_rules() function."""
    cmd = CommandListener()
    cmd.do_rules()


# Requires player input, can't test
def test_change_name():
    """Tests the do_changename() function."""
    pass


# Doesn't return anything, can't test
def test_do_highscores():
    """Tests the do_highscores() function."""
    pass


# Can't test because it requires player input
def test_do_cheat():
    """Tests the do_cheat() function."""
    pass


def test_do_quit():
    """Tests the do_quit() function."""
    cmd = CommandListener()
    should_quit = cmd.do_quit()
    assert should_quit


# Requires player input, can't test
def test_create_players():
    """Tests the create_players() function."""
    pass


# Requires player input, can't test
def test_start_game_loop():
    """Tests the start_game_loop() function."""
    pass


# Requires player input, can't test
def test_get_name_from_player():
    """Tests the get_name_from_player() function."""
    pass


# Requires player input, can't test
def test_yes_no_prompt():
    """Tests the yes_no_prompt() function."""
    pass


# Requires player input, can't test
def test_get_difficulty():
    """Tests the get_difficulty() function."""
    pass
