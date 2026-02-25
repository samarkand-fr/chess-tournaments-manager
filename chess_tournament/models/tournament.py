"""Module définissant la classe Tournament pour les tournois d'échecs."""
from typing import List
from .round import Round
from .player import Player


class Tournament:
    """Représente un tournoi d'échecs.

    Un tournoi contient des joueurs, des tours, et toutes les informations
    nécessaires pour gérer la compétition selon le système suisse.

    Attributes:
        name (str): Nom du tournoi.
        location (str): Lieu du tournoi.
        start_date (str): Date de début (YYYY-MM-DD).
        end_date (str): Date de fin (YYYY-MM-DD).
        description (str): Description du tournoi.
        num_rounds (int): Nombre total de tours (par défaut 4).
        current_round (int): Numéro du tour actuel.
        rounds (List[Round]): Liste des tours joués.
        players (List[Player]): Liste des joueurs inscrits.
    """

    def __init__(self, name, location, start_date, end_date, description,
                 num_rounds=4, current_round=1, rounds: List[Round] = None,
                 players: List[Player] = None):
        """Initialise un nouveau tournoi.

        Args:
            name (str): Nom du tournoi.
            location (str): Lieu du tournoi.
            start_date (str): Date de début.
            end_date (str): Date de fin.
            description (str): Description du tournoi.
            num_rounds (int, optional): Nombre de tours. Par défaut 4.
            current_round (int, optional): Tour actuel. Par défaut 1.
            rounds (List[Round], optional): Liste de tours. Par défaut None.
            players (List[Player], optional): Liste de joueurs. Par défaut None.
        """
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.num_rounds = num_rounds
        self.current_round = current_round
        self.rounds = rounds if rounds else []
        self.players = players if players else []

    def add_player(self, player: Player):
        """Ajoute un joueur au tournoi.

        Args:
            player (Player): Joueur à ajouter.
        """
        self.players.append(player)

    def add_round(self, round_instance: Round):
        """Ajoute un tour au tournoi.

        Args:
            round_instance (Round): Tour à ajouter.
        """
        self.rounds.append(round_instance)

    def to_dict(self):
        """Convertit le tournoi en dictionnaire pour la sérialisation.

        Returns:
            dict: Dictionnaire contenant toutes les données du tournoi.
        """
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "description": self.description,
            "num_rounds": self.num_rounds,
            "current_round": self.current_round,
            "rounds": [r.to_dict() for r in self.rounds],
            "players": [p.to_dict() for p in self.players]
        }

    @classmethod
    def from_dict(cls, data):
        """Crée une instance de Tournament à partir d'un dictionnaire.

        Args:
            data (dict): Dictionnaire contenant les données du tournoi.

        Returns:
            Tournament: Nouvelle instance de Tournament.
        """
        # Conversion des rounds (liste de dictionnaires -> liste d'objets)
        rounds_list = []
        for r_dict in data.get("rounds", []):
            rounds_list.append(Round.from_dict(r_dict))

        # Conversion des joueurs (liste de dictionnaires -> liste d'objets)
        players_list = []
        for p_dict in data.get("players", []):
            players_list.append(Player.from_dict(p_dict))

        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            description=data["description"],
            num_rounds=data.get("num_rounds", 4),
            current_round=data.get("current_round", 1),
            rounds=rounds_list,
            players=players_list
        )
