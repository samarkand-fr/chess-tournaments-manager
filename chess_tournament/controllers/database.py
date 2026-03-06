"""Module de gestion de la persistance des données en JSON.

Ce module fournit une classe Database pour gérer le chargement et la
sauvegarde des joueurs et tournois dans des fichiers JSON.
"""
import json
import os
import glob


class Database:
    """Gère la persistance des données de l'application en JSON.

    Cette classe fournit des méthodes statiques pour charger et sauvegarder
    les données des joueurs et des tournois dans des fichiers JSON.

    Attributes:
        PLAYERS_FILE (str): Chemin vers le fichier des joueurs.
        TOURNAMENTS_DIR (str): Répertoire contenant les fichiers de tournois.
    """

    PLAYERS_FILE = "data/players.json"
    TOURNAMENTS_DIR = "data/tournaments"

    def __init__(self):
        """Initialise la base de données JSON."""
        pass

    def ensure_data_dirs(self):
        """Crée les répertoires de données s'ils n'existent pas."""
        os.makedirs("data", exist_ok=True)
        os.makedirs(self.TOURNAMENTS_DIR, exist_ok=True)

    def load_players(self):
        """Charge la liste des joueurs depuis le fichier JSON."""
        self.ensure_data_dirs()
        if not os.path.exists(self.PLAYERS_FILE):
            return []
        try:
            with open(self.PLAYERS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def save_players(self, players_data):
        """Sauvegarde la liste des joueurs dans le fichier JSON."""
        self.ensure_data_dirs()
        with open(self.PLAYERS_FILE, "w") as f:
            json.dump(players_data, f, indent=4)

    def load_tournaments(self):
        """Charge tous les tournois depuis leurs fichiers JSON individuels."""
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
        """Sauvegarde un tournoi dans son fichier JSON individuel."""
        self.ensure_data_dirs()
        name = tournament_data["name"]
        safe_name = "".join(
            c for c in name if c.isalnum() or c in (' ', '-', '_')
        ).strip().replace(' ', '_')
        filename = f"{safe_name}.json"
        filepath = os.path.join(self.TOURNAMENTS_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(tournament_data, f, indent=4)
