"""JSON data persistence management module.

This module provides a Database class to manage loading and
saving players and tournaments in JSON files.
"""
import json
import os
import glob


class Database:
    """Manages application data persistence in JSON.

    This class provides methods to load and save
    player and tournament data in JSON files.

    Attributes:
        PLAYERS_FILE (str): Path to the players file.
        TOURNAMENTS_DIR (str): Directory containing tournament files.
    """

    PLAYERS_FILE = "data/players.json"
    TOURNAMENTS_DIR = "data/tournaments"

    def __init__(self):
        """Initializes the JSON database."""
        pass

    def ensure_data_dirs(self):
        """Creates data directories if they do not exist."""
        os.makedirs("data", exist_ok=True)
        os.makedirs(self.TOURNAMENTS_DIR, exist_ok=True)

    def load_players(self):
        """Loads the list of players from the JSON file."""
        self.ensure_data_dirs()
        if not os.path.exists(self.PLAYERS_FILE):
            return []
        try:
            with open(self.PLAYERS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_players(self, players_data):
        """Saves the list of players to the JSON file."""
        self.ensure_data_dirs()
        with open(self.PLAYERS_FILE, "w") as f:
            json.dump(players_data, f, indent=4)

    def load_tournaments(self):
        """Loads all tournaments from their individual JSON files."""
        self.ensure_data_dirs()
        tournaments = []
        files = glob.glob(os.path.join(self.TOURNAMENTS_DIR, "*.json"))
        for file_path in files:
            try:
                with open(file_path, "r") as f:
                    tournaments.append(json.load(f))
            except json.JSONDecodeError:
                continue
        return tournaments

    def save_tournament(self, tournament_data):
        """Saves a tournament to its individual JSON file."""
        self.ensure_data_dirs()
        name = tournament_data["name"]
        safe_name = "".join(
            c for c in name if c.isalnum() or c in (' ', '-', '_')
        ).strip().replace(' ', '_')
        filename = f"{safe_name}.json"
        filepath = os.path.join(self.TOURNAMENTS_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(tournament_data, f, indent=4)
