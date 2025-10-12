class HighScore:
    def __init__(self, name, games_played = 0, games_wom = 0):
        self.name = name
        self.games_played = games_played
        self.games_won = games_wom

    def increment_games_won(self):
        self.games_won += 1

    def increment_games_played(self):
        self.games_played += 1

    def __str__(self):
        return f"{self.name} {self.games_played} {self.games_won}"


def from_persisted_line(line):
    (name, games_played, games_won) = line.split()
    return HighScore(name, int(games_played), int(games_won))
