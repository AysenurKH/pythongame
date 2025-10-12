"""The main file for this application.

It contains a class CommandListener which inherits from the Cmd class in the command module.
The command loop is started automatically.
"""

import cmd
from src.player import Player
from src.intelligence import Intelligence
from src.game import Game
from src import high_score

RULES = """
Welcome to the Dice game "Pig".
This game is played with 2 players. You can play against a friend, or against the computer.
Player 1 starts.
Keep rolling one die at a time and sum the value of each throw.
At any point, you can decide to stop rolling dice, and the points you've collected so far in this round are
 added to your score.
If you roll a 1 though, your turn ends and you do not get to keep these points.
Once your turn ends, it's player 2's turn. Once their turn ends, it's your turn again, and so on.
First player to reach 100 points wins.
"""


class CommandListener(cmd.Cmd):
    """Inherits from the Cmd module.

    This means that any methods with defined in this class with names of the format "do_xxx()" can be executed by
    simply typing xxx in the terminal.
    """

    intro = "Welcome to the Pig dice game.   Type help or ? to list commands.\n"
    prompt = "Input: "
    player1 = None
    player2 = None

    def __init__(self):
        """The constructor."""
        super().__init__()

    def do_play(self, *_):
        """Starts the game.

        Args
        -------
        - `arg:` Not used

        Returns
        -------
        - `void:` The Cmd module will automatically wait for another command.
        """
        self.start_game_loop(cheat=False)

    def do_rules(self, *_):
        """View the rules of the game.

        Args
        -------
        - `arg:` Not used

        Returns
        -------
        - `void:` The Cmd module will automatically wait for another command.
        """
        print(RULES)

    def do_changename(self, arg):
        """Set name of player by their player number.

        Args
        -------
        - `arg:` The number of the player you wish to change the name of. Pick between 1 or 2

        Returns
        -------
        - `void:` The Cmd module will automatically wait for another command.
        """
        try:
            player_number = int(arg)
        except ValueError:
            print("player number must be a single integer")
            return

        if player_number not in (1, 2):
            print("The player number must be either 1 or 2")
            return

        player = self.player1 if player_number == 1 else self.player2

        if not player:
            print(f"Player {player_number} does not exist. Play a game first")
            return

        print(f"Renaming {player.name}..")
        new_name = get_name_from_player(player_number)
        current_name = player.name
        player.set_name(new_name)
        print(f"Player {current_name} has changed name to {new_name}")

    def do_highscores(self, *_):
        """Displays the scores from all previous games.

        Args
        -------
        - `arg:` Not used

        Returns
        -------
        - `void:` The Cmd module will automatically wait for another command.
        """
        high_scores = high_score.get_high_scores()
        print(f"{'Name':<20} {'Games Won':<10} {'Games Played':<10}")
        print("-" * 35)
        for hs in high_scores.values():
            print(f"{hs.name:<20} {hs.games_won:<10} {hs.games_played:<10}")

    def do_cheat(self, *_):
        """Plays a normal game, but player 1 starts with 99 points in their hand.

        Args
        -------
        - `arg:` Not used

        Returns
        -------
        - `void:` The Cmd module will automatically wait for another command.
        """
        self.start_game_loop(cheat=True)

    def do_quit(self, *_):
        """Quits the game.

        Args
        -------
        - `arg:` Not used

        Returns
        -------
        - `bool:` True, which makes the Cmd module quit and stop listening for more commands.
        """
        print("Thank you for playing Pig!")
        return True

    def create_players(self):
        """Creates the 2 players if they don't already exists, and stores them globally for next games."""
        if self.player1 or self.player2:
            # No need to ask players for their names if they have just played a game previously
            return
        name_player1 = get_name_from_player(1)
        self.player1 = Player(name_player1)

        play_against_computer = yes_no_prompt("Play against computer? [y/n]")
        if play_against_computer:
            difficulty = get_difficulty()
            self.player2 = Intelligence(difficulty)
        else:
            name_player2 = get_name_from_player(2)
            self.player2 = Player(name_player2)

    def start_game_loop(self, cheat=False):
        """Starts the game loop.

        Args
        ----
        - `cheat:` If True, player 1 will start the game with 99 points in their dice hand.
        """
        self.create_players()
        game = Game(self.player1, self.player2, cheat)
        game.start_game_loop()
        print(self.intro)


def get_name_from_player(player_number):
    """Ask the player for their name.

    Args
    -------
    - `player_number:` The number of the player. Either 1 or 2. Used in the terminal prompt.

    Returns
    -------
    - `str:` Non-blank string representing the player's name
    """
    name = None
    while not name:
        name = input(f"Player {player_number} name: ")
        if not name:
            print("Name must be a non-blank string")
    return name


def yes_no_prompt(text):
    """Displays a yes-no prompt in the terminal.

    Args
    -------
    - `text:` The text to present the player in the terminal.

    Returns
    -------
    - `bool:` Return True if the player typed "y" or "Y". Returns False if the player typed "n" or "N".
    The player will continue to be asked until they provide one of these options.
    """
    choice = None
    while not choice or choice.lower() not in ("y", "n"):
        choice = input(text)
    return choice.lower() == "y"


def get_difficulty():
    """Asks the player for the difficulty level of the computer that they play against.

    Returns
    -------
    - `int:` Returns either 1, 2 or 3. 1 is the easiest setting, and 3 is the hardest.
    """
    print("You are playing against the computer")
    while True:
        try:
            value = int(input("Pick a difficulty: 1 (EASY), 2 (MEDIUM), 3 (HARD)"))
        except ValueError:
            print("Bad input")
            continue
        if 0 <= value <= 3:
            return value
        print("Pick a number between 1 and 3")


if __name__ == "__main__":
    CommandListener().cmdloop()
