import json
import os
import glob


class Database:
    # Gère la persistance des données de l'application en JSON.

    PLAYERS_FILE = "data/players.json"
    TOURNAMENTS_DIR = "data/tournaments"

    @classmethod
    def ensure_data_dirs(cls):
        """Crée les répertoires de données s'ils n'existent pas."""
        os.makedirs("data", exist_ok=True)
        os.makedirs(cls.TOURNAMENTS_DIR, exist_ok=True)

    @classmethod
    def load_players(cls):
        # Charge la liste des joueurs depuis le fichier JSON.

        cls.ensure_data_dirs()
        if not os.path.exists(cls.PLAYERS_FILE):
            return []
        try:
            with open(cls.PLAYERS_FILE, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    @classmethod
    def save_players(cls, players_data):
        # Sauvegarde la liste des joueurs dans le fichier JSON.

        cls.ensure_data_dirs()
        with open(cls.PLAYERS_FILE, "w") as f:
            json.dump(players_data, f, indent=4)

    @classmethod
    def load_tournaments(cls):
        # Charge tous les tournois depuis leurs fichiers JSON individuels.

        cls.ensure_data_dirs()
        tournaments = []
        files = glob.glob(os.path.join(cls.TOURNAMENTS_DIR, "*.json"))
        for file_path in files:
            try:
                with open(file_path, "r") as f:
                    tournaments.append(json.load(f))
            except json.JSONDecodeError:
                continue
        return tournaments

    @classmethod
    def save_tournament(cls, tournament_data):
        # Sauvegarde un tournoi dans son fichier JSON individuel.

        cls.ensure_data_dirs()
        name = tournament_data["name"]
        safe_name = "".join(
            c for c in name if c.isalnum() or c in (' ', '-', '_')
        ).strip().replace(' ', '_')
        filename = f"{safe_name}.json"
        filepath = os.path.join(cls.TOURNAMENTS_DIR, filename)

        with open(filepath, "w") as f:
            json.dump(tournament_data, f, indent=4)
