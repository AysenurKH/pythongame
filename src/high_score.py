"""Code related to the persisted high scores of players."""

import os

FILE_NAME = "highscore.txt"


class HighScore:
    """Class representing a single player's game stats."""

    def __init__(self, name, games_played=0, games_wom=0):
        """Constructor.

        Args
        ----
        - `name:` str, name of the player.
        - `games_played:` int, number of games this player has played.
        - `games_wom:` int, number of games this player has won.
        """
        self.name = name
        self.games_played = games_played
        self.games_won = games_wom

    def increment_games_won(self):
        """Adds 1 to the number of games won."""
        self.games_won += 1

    def increment_games_played(self):
        """Adds 1 to the number of games played."""
        self.games_played += 1

    def __str__(self):
        """Overrides the default __str__ method.

        This means that if we ever try to print a HighScore object, it will print with the format defined below.
        This is used when writing high scores consistently to a file.

        Returns
        -------
        - `str:` All fields in the class separated by spaces.
        """
        return f"{self.name} {self.games_played} {self.games_won}"


def from_persisted_line(line):
    """Takes a line from the persisted high scores file and converts it to a HighScore object.

    Args
    ----
    - `line:` str, A single line from the persisted high scores file.

    Returns
    -------
    - `HighScore:` A HighScore object representing the data from the line which was read from the persisted high score
    file.
    """
    (name, games_played, games_won) = line.split()
    return HighScore(name, int(games_played), int(games_won))


def persist_win(winning_player, losing_player):
    """Updates the persisted high score file with data about the players who just played.

    If the file doesn't exist, it is created.
    If the players do not exist in the file, they are added.
    If the players already exist, their stats are updated.

    Args
    ----
    - `winning_player:` Player, the player who just won.
    - `losing_player:` Player, the player who just lost.
    """
    # First load the existing high scores
    high_scores = get_high_scores()

    # Ensure both players exist in the dict
    for player in (winning_player, losing_player):
        high_scores.setdefault(player.name, HighScore(player.name))

    # Next, update the stats for the winning player and losing player
    high_scores[winning_player.name].increment_games_won()
    for player in (winning_player, losing_player):
        high_scores[player.name].increment_games_played()

    # Finally, store it all back in the file
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for high_score in high_scores.values():
            # You can print to files, while specifying line separator. This avoids a linebreak at the end of the file,
            # causing an empty line at the bottom
            # the HighScore class overrides the __str__ method, which formats the high score correctly in the file.
            print(high_score, sep=os.linesep, file=file)


def get_high_scores():
    """Gets all the currently persisted high scores.

    Returns
    -------
    - `dict[str, list[HighScore]]:` All persisted stats. Each line is an entry in the dict.
    The key represents the player's name, and the value is a HighScore object.
    """
    high_scores = {}
    if os.path.isfile(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                high_score = from_persisted_line(line)
                high_scores[high_score.name] = high_score
    return high_scores
