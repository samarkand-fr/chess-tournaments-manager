"""Module defining the Tournament class for chess tournaments."""
from typing import List
from .round import Round
from .player import Player


class Tournament:
    """Represents a chess tournament.

    A tournament contains players, rounds, and all the information
    necessary to manage the competition according to the Swiss system.

    Attributes:
        name (str): Tournament name.
        location (str): Tournament location.
        start_date (str): Start date (YYYY-MM-DD).
        end_date (str): End date (YYYY-MM-DD).
        description (str): Tournament description.
        num_rounds (int): Total number of rounds (default 4).
        current_round (int): Current round number.
        rounds (List[Round]): List of rounds played.
        players (List[Player]): List of registered players.
    """

    def __init__(self, name, location, start_date, end_date, description,
                 num_rounds=4, current_round=1, rounds: List[Round] = None,
                 players: List[Player] = None):
        """Initializes a new tournament.

        Args:
            name (str): Tournament name.
            location (str): Tournament location.
            start_date (str): Start date.
            end_date (str): End date.
            description (str): Tournament description.
            num_rounds (int, optional): Number of rounds. Defaults to 4.
            current_round (int, optional): Current round. Defaults to 1.
            rounds (List[Round], optional): List of rounds. Defaults to None.
            players (List[Player], optional): List of players. Defaults to None.
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
        """Adds a player to the tournament.

        Args:
            player (Player): Player to add.
        """
        self.players.append(player)

    def add_round(self, round_instance: Round):
        """Adds a round to the tournament.

        Args:
            round_instance (Round): Round to add.
        """
        self.rounds.append(round_instance)

    def to_dict(self):
        """Converts the tournament to a dictionary for serialization.

        Returns:
            dict: Dictionary containing all tournament data.
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
        """Creates a Tournament instance from a dictionary.

        Args:
            data (dict): Dictionary containing tournament data.

        Returns:
            Tournament: New Tournament instance.
        """
        # Convert rounds (list of dictionaries -> list of objects)
        rounds_list = []
        for r_dict in data.get("rounds", []):
            rounds_list.append(Round.from_dict(r_dict))

        # Convert players (list of dictionaries -> list of objects)
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
