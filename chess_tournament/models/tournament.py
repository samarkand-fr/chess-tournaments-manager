from typing import List
from .round import Round
from .player import Player


class Tournament:
    # Représente un tournoi d'échecs.

    def __init__(self, name, location, start_date, end_date, description,
                num_rounds=4, current_round=1, rounds: List[Round] = None,
                players: List[Player] = None):

        # Initialise un nouveau tournoi.
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
        #Ajoute un joueur au tournoi.
        self.players.append(player)

    def add_round(self, round_instance: Round):
        # Ajoute un tour au tournoi.

        self.rounds.append(round_instance)

    def to_dict(self):
        # Convertit le tournoi en dictionnaire pour la sérialisation.

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

    @staticmethod
    def from_dict(data):
        # Crée une instance de Tournament à partir d'un dictionnaire.

        
        rounds_list = []
        # Conversion des rounds (liste de dictionnaires -> liste d'objets)
        for r_dict in data.get("rounds", []):
            rounds_list.append(Round.from_dict(r_dict))
       
        players_list = []
         # Conversion des joueurs (liste de dictionnaires -> liste d'objets)
        for p_dict in data.get("players", []):
            players_list.append(Player.from_dict(p_dict))

        return Tournament(
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
